from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from typing import Any

@api_view(['POST'])
def api_home(request: HttpRequest) -> Response:
    response_object = {}

    try:
        data = json.loads(request.body)
        if isinstance(data, dict):
            response_object["payload"] = data
        else:
            response_object["payload"] = {}
    except json.JSONDecodeError:
        response_object["payload"] = {}

    # Step 3: Convert string into an array of characters
    payload: dict[str, Any] = response_object.get("payload", {})
    data_value = payload.get("data", "")

    if isinstance(data_value, str):
        char_array = list(data_value)
    else:
        char_array = []

    # Step 4: Sort the array alphabetically
    sorted_array = sorted(char_array)

    # Step 5: Return the sorted array in JSON format
    result = {
        "word": sorted_array
    }

    json_result = json.dumps(result)
    print(json_result)

    return Response(result)
