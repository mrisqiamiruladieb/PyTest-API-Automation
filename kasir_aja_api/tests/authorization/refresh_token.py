# import required modules
import requests
import json
from jsonschema import validate

# Set the base url
BASE_URL = "https://kasir-api.belajarqa.com"


def test_success_refresh_token():

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
                    }
                },
                "required": [
                    "accessToken"
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
        "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjlmZDcwOTZkLTEwMDItNGVjNy04NzFmLTdmMGI0ODEwODExOSIsImNvbXBhbnlJZCI6Ijg4YzBjZTMzLTRmOGEtNGRiNS05YzMxLWVmNGU3Yzg2OGJmZiIsImlhdCI6MTcxOTk5MDM4N30.sExFUFe4D4Jk3gLv68U_NL6kVmRHg4ydAUl1KMcXHzs"
    }

    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjlmZDcwOTZkLTEwMDItNGVjNy04NzFmLTdmMGI0ODEwODExOSIsImNvbXBhbnlJZCI6Ijg4YzBjZTMzLTRmOGEtNGRiNS05YzMxLWVmNGU3Yzg2OGJmZiIsImlhdCI6MTcxOTk5MDM4N30.VG6197JBwJ70QoSYKsjoC1s722Hs9eTuRTqaCu1jhw0"

    headers = {"Authorization": f"Bearer {access_token}",
               "Content-Type": "application/json"}

    # Making a put request
    response = requests.put(BASE_URL + "/authentications", json=payload, headers=headers)

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

    # Asserting Response Headers
    assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type

    # is empty response body
    assert len(string_resp_body) != 0, "Unexpected Response Body Length " + \
        str(len(string_resp_body))
    assert len(str(respJson.get("status"))) != 0, "Unexpected Response Body Length " + \
        str(len(str(respJson.get("status"))))

    # check the substring in the response body
    assert bool("Access Token berhasil diperbarui" in string_resp_body) == True

    validate(instance=respJson, schema=jsonSchema)
    # No error, the JSON is valid.
