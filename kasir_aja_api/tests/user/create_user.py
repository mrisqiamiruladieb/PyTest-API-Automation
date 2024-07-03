# import required modules
import requests
import json
from jsonschema import validate
import random
from ...helper.get_access_token import success_get_access_token

# Set the base url
BASE_URL = "https://kasir-api.belajarqa.com"


def test_success_create_user():

    jsonSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
            "status": {
                "type": "string"
            },
            "message": {
                "type": "string"
            },
            "data": {
                "type": "object",
                "properties": {
                    "userId": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    }
                },
                "required": [
                    "userId",
                    "name"
                ]
            }
        },
        "required": [
            "status",
            "message",
            "data"
        ]
    }

    # Generate random number
    rand_int = random.randint(1, 999)

    payload = {
        "name": "kasir-" + str(rand_int),
        "email": "user-" + str(rand_int) + "@example.com",
        "password": "jiasda2321@"
    }

    access_token = success_get_access_token()

    headers = { "Authorization": f"Bearer {access_token}" }

    # Making a post request
    response = requests.post(BASE_URL + "/users", data=payload, headers=headers)

    # Convert json into dictionary
    respJson = response.json()

    # Convert json into string
    string_resp_body = str(respJson)

    print("\n------------Request------------")

    print("Method : ", response.request)
    print("Url : ", response.url)
    print("Request Body :\n", json.dumps(payload, indent=4, sort_keys=False))

    print("\n------------Response------------")

    # print response status code
    print("Response Status Codes: ", response.status_code, response.reason)

    # Pretty Printing JSON string back
    print("Response Body:\n", json.dumps(respJson, indent=4, sort_keys=False))

    # get response headers
    content_type = response.headers.get("Content-Type")

    # assert
    assert response.status_code == 201, "Unexpected status code: " + \
        str(response.status_code)

    # Asserting Response Headers
    assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type

    # is empty response body
    assert len(string_resp_body) != 0, "Unexpected Response Body Length " + \
        str(len(string_resp_body))
    assert len(str(respJson.get("status"))) != 0, "Unexpected Response Body Length " + \
        str(len(str(respJson.get("status"))))

    # check the substring in the response body
    assert bool("User berhasil ditambahkan" in string_resp_body) == True

    validate(instance=respJson, schema=jsonSchema)
    # No error, the JSON is valid.