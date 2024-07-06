# import required modules
import requests
import json
from jsonschema import validate
from ...helper.get_access_token import success_get_access_token
from ...helper.get_user_name import success_get_user_name

# Set the base url
BASE_URL = "https://kasir-api.belajarqa.com"


def test_success_get_user_list():

    jsonSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
            "status": {
                "type": "string"
            },
            "data": {
                "type": "object",
                "properties": {
                    "users": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "email": {
                                    "type": "string"
                                },
                                "role": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "name",
                                "email",
                                "role"
                            ]
                        }
                    },
                    "meta": {
                        "type": "object",
                        "properties": {
                            "totalPages": {
                                "type": "number"
                            },
                            "total": {
                                "type": "number"
                            },
                            "page": {
                                "type": "number"
                            }
                        },
                        "required": [
                            "totalPages",
                            "total",
                            "page"
                        ]
                    }
                },
                "required": [
                    "users",
                    "meta"
                ]
            }
        },
        "required": [
            "status",
            "data"
        ]
    }

    # get access token using helper
    access_token = success_get_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # get user name using helper
    user_name = success_get_user_name()

    # create a get request using query params
    query_params = {
        'q': user_name,
        'p': 1,
    }

    response = requests.get(
        BASE_URL + "/users", params=query_params, headers=headers)

    # Convert json into dictionary
    response_json = response.json()

    # Convert json into string
    string_resp_body = str(response_json)

    print("\n------------Request------------")

    print("Method : ", response.request)
    print("Url : ", response.url)

    print("\n------------Response------------")

    # print response status code
    print("Response Status Codes: ", response.status_code, response.reason)

    # Pretty Printing JSON string back
    print("Response Body:\n", json.dumps(
        response_json, indent=4, sort_keys=False))

    # get response headers
    content_type = response.headers.get("Content-Type")

    # assert
    assert response.status_code == 200, "Unexpected status code: " + \
        str(response.status_code)

    # Asserting Response Headers
    assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type

    # access users[0].id
    # hello = response_json['data']['users'][0]
    # print("this is id: " + hello['id'])

    # assert user name
    assert user_name == response_json.get('data').get('users')[0].get('name'), "Unexpected user name: " + user_name

    # is empty response body
    assert len(string_resp_body) != 0, "Unexpected Response Body Length " + \
        str(len(string_resp_body))
    assert len(str(response_json.get("status"))) != 0, "Unexpected Response Body Length " + \
        str(len(str(response_json.get("status"))))

    # check the substring in the response body
    assert bool("id" and "email" and "role" in string_resp_body) == True

    validate(instance=response_json, schema=jsonSchema)
    # No error, the JSON is valid.
