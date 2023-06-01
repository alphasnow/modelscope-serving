from typing import Callable

from fastapi import FastAPI


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    def start_app() -> None:
        """
        @app.post("/predict/chinese-segment")
        def post_chinese_segment(request: Request):
            # request.state.model_manager.chinese_segment.handle(text="测试拆分文字")
            pass
        """
        pass

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    def stop_app() -> None:
        pass

    return stop_app
