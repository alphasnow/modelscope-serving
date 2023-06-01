from typing import Union

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import validation_error_response_definition
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import (HTTP_422_UNPROCESSABLE_ENTITY,
                              HTTP_500_INTERNAL_SERVER_ERROR)


# https://github.com/nsidnev/fastapi-realworld-example-app/blob/master/app/api/errors/validation_error.py
def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse({
        "errors": [exc.detail],
        "type": str(type(exc)),
        "msg": "error",
    }, status_code=exc.status_code)


def error_handler(_: Request, exc: Exception) -> JSONResponse:
    return JSONResponse({
        "errors": [str(exc)],
        "type": str(type(exc)),
        "msg": "error",
    }, status_code=HTTP_500_INTERNAL_SERVER_ERROR)


def http422_error_handler(
        _: Request,
        exc: Union[RequestValidationError, ValidationError],
) -> JSONResponse:
    return JSONResponse(
        {"errors": exc.errors()},
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )


validation_error_response_definition["properties"] = {
    "errors": {
        "title": "Errors",
        "type": "array",
        "items": {"$ref": "{0}ValidationError".format(REF_PREFIX)},
    },
}
