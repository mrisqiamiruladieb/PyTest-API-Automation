# import required modules
import requests
import json
from jsonschema import validate

# Set the base url
BASE_URL = "https://reqres.in"


def test_success_create_user():

    jsonSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
            "name": {
                "type": "string"
            },
            "job": {
                "type": "string"
            },
            "id": {
                "type": "string"
            },
            "createdAt": {
                "type": "string"
            }
        },
        "required": [
            "name",
            "job",
            "id",
            "createdAt"
        ]
    }

    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    # Making a post request
    response = requests.post(BASE_URL + "/api/users", data=payload)

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

    # Parse the request body
    name_request = payload.get("name")
    job_request = payload.get("job")

    # assert
    assert response.status_code == 201, "Unexpected status code: " + \
        str(response.status_code)
    assert respJson.get("name") == name_request
    assert respJson.get("job") == job_request

    # Asserting Response Headers
    assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type

    # is empty response body
    assert len(string_resp_body) != 0, "Unexpected Response Body Length " + \
        str(len(string_resp_body))
    assert len(str(respJson.get("id"))) != 0, "Unexpected Response Body Length " + \
        str(len(str(respJson.get("id"))))
    assert len(str(respJson.get("createdAt"))) != 0, "Unexpected Response Body Length " + \
        str(len(str(respJson.get("createdAt"))))

    # check the substring in the response body
    assert bool("id" in string_resp_body) == True
    assert bool("createdAt" in string_resp_body) == True

    validate(instance=respJson, schema=jsonSchema)
    # No error, the JSON is valid.
