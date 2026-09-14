# syntax=docker/dockerfile:1

FROM python:3.12-slim

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 从 PyPI 安装 uv(相比从 ghcr.io 拉取 uv 镜像更可靠, 避免偶发的下载卡顿)
RUN pip install --no-cache-dir uv

# 只拷贝依赖清单，利用 Docker 层缓存加速重复构建
# 说明: 项目运行时依赖 flasgger/flask-admin(位于 dev 分组)，故这里用默认 uv sync 一并安装
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

# 拷贝源码并安装项目本身
COPY . .
RUN uv sync --frozen

EXPOSE 8080

# 使用 Gunicorn 启动生产服务
# 对于快速启动/本地演示场景，单 worker 完全够用
CMD ["uv", "run", "gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "server:app"]