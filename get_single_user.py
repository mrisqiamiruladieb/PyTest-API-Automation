# import required modules
import requests
import json
from jsonschema import validate

# Set the base url
BASE_URL = "https://reqres.in"


def test_success_get_single_user():
    jsonSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
            "data": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "number"
                    },
                    "email": {
                        "type": "string"
                    },
                    "first_name": {
                        "type": "string"
                    },
                    "last_name": {
                        "type": "string"
                    },
                    "avatar": {
                        "type": "string"
                    }
                },
                "required": [
                    "id",
                    "email",
                    "first_name",
                    "last_name",
                    "avatar"
                ]
            },
            "support": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string"
                    },
                    "text": {
                        "type": "string"
                    }
                },
                "required": [
                    "url",
                    "text"
                ]
            }
        },
        "required": [
            "data",
            "support"
        ]
    }

    url = BASE_URL + "/api/users/"

    path_params = "2"

    # Making a get request
    response = requests.get(url + path_params)

    # Convert json into dictionary
    respJson = response.json()

    # Convert json into string
    string_resp_body = str(respJson)

    print("\n------------Request------------")

    print("Method : ", response.request)
    print("Url : ", response.url)

    print("\n------------Response------------")

    # print response status code
    print("Response Status Codes: ", response.status_code, response.reason)

    # Pretty Printing JSON string back
    print("Response Body:\n", json.dumps(respJson, indent=4, sort_keys=False))

    # get response headers
    content_type = response.headers.get("Content-Type")

    # assert
    assert response.status_code == 200, "Unexpected status code: " + \
        str(response.status_code)
    assert respJson.get("data").get("id") == 2
    assert respJson.get("data").get("first_name") == "Janet"

    # Asserting Response Headers
    assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type

    # is empty response body
    assert len(string_resp_body) != 0, "Unexpected Response Body Length " + \
        str(len(string_resp_body))
    assert len(str(respJson.get("data").get("id"))) != 0, "Unexpected Response Body Length " + \
        str(len(str(respJson.get("data").get("id"))))
    assert len(str(respJson.get("data").get("last_name"))) != 0, "Unexpected Response Body Length " + \
        str(len(str(respJson.get("data").get("last_name"))))

    # check the substring in the response body
    assert bool("avatar" in string_resp_body) == True
    assert bool("To keep" in string_resp_body) == True

    validate(instance=respJson, schema=jsonSchema)
    # No error, the JSON is valid.
