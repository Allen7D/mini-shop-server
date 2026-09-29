# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
  Updated to use Flask CLI instead of flask-script
"""
import sys

from werkzeug.middleware.proxy_fix import ProxyFix
import click

from app import create_app

__author__ = 'Allen7D'

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.cli.command("run")
@click.option('--host', '-h', default='127.0.0.1', help='The host to bind to.')
@click.option('--port', '-p', default=5000, help='The port to bind to.')
@click.option('--debug', is_flag=True, help='Enable debug mode.')
def run_command(host, port, debug):
    """Run the Flask development server."""
    app.run(host=host, port=port, debug=debug)

def main(argv=None):
    # No args keeps the old `python server.py` default. `run -h/-p` is what the README documents.
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        app.run()
        return
    app.cli.main(args=list(argv), prog_name='server.py', standalone_mode=False)

if __name__ == '__main__':
    main()
