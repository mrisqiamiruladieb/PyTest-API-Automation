# import required modules 
import requests
import json
from jsonschema import validate

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

    url = "https://reqres.in/api/users?page=2"

    # Making a get request 
    response = requests.get(url)

    # Convert json into dictionary 
    respJson = response.json()

    # print response status code
    print("\nResponse Status Codes: ", response.status_code)

    # print response 
    # print("\nResponse: ", response)

    # Pretty Printing JSON string back 
    print("Response Body:\n", json.dumps(respJson, indent=4, sort_keys=True))

    # assert
    assert response.status_code == 200
    assert respJson.get('page') == 2

    validate(instance=respJson, schema=jsonSchema)
    # No error, the JSON is valid.