# import required modules
import requests
import json
from jsonschema import validate

# Set the base url
BASE_URL = "https://kasir-api.belajarqa.com"


def test_success_login():

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
                    "accessToken": {
                        "type": "string"
                    },
                    "refreshToken": {
                        "type": "string"
                    },
                    "user": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "role": {
                                "type": "string"
                            },
                            "email": {
                                "type": "string"
                            },
                            "officeId": {
                                "type": "string"
                            },
                            "companyId": {
                                "type": "string"
                            },
                            "company_name": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "name",
                            "role",
                            "email",
                            "officeId",
                            "companyId",
                            "company_name"
                        ]
                    }
                },
                "required": [
                    "accessToken",
                    "refreshToken",
                    "user"
                ]
            }
        },
        "required": [
            "status",
            "message",
            "data"
        ]
    }

    payload = {
        "email": "hello@gmail.com",
        "password": "12345678",
    }

    # Making a post request
    response = requests.post(BASE_URL + "/authentications", data=payload)

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

    # Parse the request body
    email_request = payload.get('email')

    # Parse the response body
    email_response = respJson.get('data').get('user').get('email')

    # get response headers
    content_type = response.headers.get("Content-Type")

    # assert
    assert response.status_code == 201, "Unexpected status code: " + \
        str(response.status_code)
    assert email_response == email_request, "Unexpected email: " + email_request

    # Asserting Response Headers
    assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type

    # is empty response body
    assert len(string_resp_body) != 0, "Unexpected Response Body Length " + \
        str(len(string_resp_body))
    assert len(str(respJson.get("status"))) != 0, "Unexpected Response Body Length " + \
        str(len(str(respJson.get("status"))))

    # check the substring in the response body
    assert bool("Authentication berhasil ditambahkan" in string_resp_body) == True

    validate(instance=respJson, schema=jsonSchema)
    # No error, the JSON is valid.
