# import required modules
import requests
import json
from jsonschema import validate

# Set the base url
BASE_URL = "https://reqres.in"


def test_success_update_user():
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
            "updatedAt": {
                "type": "string"
            }
        },
        "required": [
            "name",
            "job",
            "updatedAt"
        ]
    }

    url = BASE_URL + "/api/users/"

    path_params = "2"

    payload = {
        "name": "morpheus-update",
        "job": "zion resident-update"
    }

    # Making a put request
    response = requests.put(url + path_params, data=payload)

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
    name_request = payload.get('name')
    job_request = payload.get('job')

    # get response headers
    content_type = response.headers.get("Content-Type")

    # assert
    assert response.status_code == 200, "Unexpected status code: " + \
        str(response.status_code)
    assert respJson.get("name") == name_request
    assert respJson.get("job") == job_request

    # Asserting Response Headers
    assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type

    # is empty response body
    assert len(string_resp_body) != 0, "Unexpected Response Body Length " + \
        str(len(string_resp_body))
    assert len(str(respJson.get("updatedAt"))) != 0, "Unexpected Response Body Length " + \
        str(len(str(respJson.get("updatedAt"))))
    
    # check the substring in the response body
    assert bool("update" in string_resp_body) == True
    assert bool("zion" in string_resp_body) == True

    validate(instance=respJson, schema=jsonSchema)
    # No error, the JSON is valid.
