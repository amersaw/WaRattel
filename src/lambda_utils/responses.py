import json
from typing import Optional

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
}


def error_response(
    error_message: str,
    error_code: int,
    allow_cors=True,
):
    return {
        "headers": {
            "content-type": "application/json",
            **(CORS_HEADERS if allow_cors else {}),
        },
        "statusCode": error_code,
        "body": json.dumps({"error": error_message}),
    }


def success_response(
    obj: dict,
    response_code: int = 200,
    content_type="application/json",
    allow_cors=True,
    dump_body_json=True,
    is_b64_encoded: Optional[bool] = None,
):
    res = {
        "headers": {
            "content-type": content_type,
            **(CORS_HEADERS if allow_cors else {}),
        },
        "statusCode": response_code,
        "body": json.dumps(obj) if dump_body_json else obj,
    }
    if not (is_b64_encoded is None):
        res.update({"isBase64Encoded": is_b64_encoded})
    return res
