# _*_ coding: utf-8 _*_
import sys
from unittest.mock import patch

from flask import Flask


def _load_server():
    # Importing server normally opens the configured database. Keep this test off that path.
    sys.modules.pop("server", None)
    with patch("app.create_app", return_value=Flask(__name__)):
        import server
    return server


def test_readme_run_flags_are_accepted_and_forwarded():
    server = _load_server()
    command = server.app.cli.commands["run"]
    params = command.make_context("run", ["-h", "0.0.0.0", "-p", "8080"]).params
    assert params == {"host": "0.0.0.0", "port": 8080, "debug": False}

    called = {}

    def fake_run(host="127.0.0.1", port=5000, debug=False, **kwargs):
        called.clear()
        called.update(host=host, port=port, debug=debug)

    server.app.run = fake_run
    command.callback.__wrapped__(**params)
    assert called == {"host": "0.0.0.0", "port": 8080, "debug": False}

    forwarded = {}

    def fake_main(args=None, prog_name=None, **kwargs):
        forwarded["args"] = list(args)
        forwarded["prog_name"] = prog_name
        forwarded["standalone_mode"] = kwargs.get("standalone_mode")

    server.app.cli.main = fake_main
    server.main(["run", "-h", "0.0.0.0", "-p", "8080"])
    assert forwarded == {
        "args": ["run", "-h", "0.0.0.0", "-p", "8080"],
        "prog_name": "server.py",
        "standalone_mode": False,
    }

    server.main([])
    assert called == {"host": "127.0.0.1", "port": 5000, "debug": False}
