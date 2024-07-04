# import required modules
import requests
import json
from jsonschema import validate

# Set the base url
BASE_URL = "https://reqres.in"

def test_get_list_of_users():

    jsonSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generated schema for Root",
        "type": "object",
        "properties": {
            "data": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "avatar": {
                            "type": "string"
                        },
                        "email": {
                            "type": "string"
                        },
                        "first_name": {
                            "type": "string"
                        },
                        "id": {
                            "type": "number"
                        },
                        "last_name": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "avatar",
                        "email",
                        "first_name",
                        "id",
                        "last_name"
                    ]
                }
            },
            "page": {
                "type": "number"
            },
            "support": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string"
                    },
                    "url": {
                        "type": "string"
                    }
                },
                "required": [
                    "text",
                    "url"
                ]
            },
            "total": {
                "type": "number"
            },
            "total_pages": {
                "type": "number"
            }
        },
        "required": [
            "data",
            "page",
            "support",
            "total",
            "total_pages"
        ]
    }

    url = BASE_URL + "/api/users"

    query_params = {
        'page': 2,
    }

    # Making a get request
    response = requests.get(url, params=query_params)

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

    # print response
    # print("\nResponse: ", response)

    # Pretty Printing JSON string back
    print("Response Body:\n", json.dumps(respJson, indent=4, sort_keys=False))

    # get response headers
    content_type = response.headers.get("Content-Type")

    # assert
    assert response.status_code == 200, "Unexpected status code: " + \
        str(response.status_code)
    assert respJson.get('page') == 2

    # Access data[0].id
    # accesses the id field of the first data object in the data array of the respJson dictionary
    first_user_id = respJson['data'][0]['id']
    # print("first user id : ", first_user_id)
    assert first_user_id == 7, "Unexpected first user id: " + str(first_user_id)

    # Access data[1].last_name
    second_user_last_name = respJson.get('data')[1].get('last_name')
    # print("Second user last name : ", second_user_last_name)
    assert second_user_last_name == "Ferguson", "Unexpected second user last name: " + second_user_last_name
    
    # Asserting Response Headers
    assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type

    # is empty response body
    assert len(string_resp_body) != 0, "Unexpected Response Body Length " + \
        str(len(string_resp_body))
    assert len(str(respJson.get("page"))) != 0, "Unexpected Response Body Length " + \
        str(len(str(respJson.get("page"))))

    # check the substring in the response body
    assert bool("2" in string_resp_body) == True

    validate(instance=respJson, schema=jsonSchema)
    # No error, the JSON is valid.
