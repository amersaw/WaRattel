
from typing import Any, Dict, Optional


def get_query_param(event: Dict[str, Any], paramName: str) -> Optional[str]:
    if "pathParameters" in event and paramName in event["pathParameters"]:
        return event["pathParameters"][paramName]
    if "queryStringParameters" in event and paramName in event["queryStringParameters"]:
        return event["queryStringParameters"][paramName]
    return None
