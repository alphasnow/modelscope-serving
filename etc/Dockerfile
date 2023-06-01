FROM registry.cn-hangzhou.aliyuncs.com/modelscope-repo/modelscope:ubuntu20.04-py37-torch1.11.0-tf1.15.5-1.1.2

# httpx pytest pytest-asyncio for debug
RUN pip install fastapi==0.88.0 uvicorn==0.20.0 \
    loguru python-multipart \
    httpx pytest pytest-asyncio;
