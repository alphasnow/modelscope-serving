import time

from fastapi import APIRouter

router = APIRouter()


@router.get('/timestamp')
def get_timestamp():
    return {
        "timestamp": int(time.time()),
        "datetime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }
