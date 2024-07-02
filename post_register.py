# import required modules 
import requests
import json
from jsonschema import validate

def test_successful_registration():

    jsonSchema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "id": {
      "type": "number"
    },
    "token": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "token"
  ]
}
    
    url = "https://reqres.in/api/register"

    payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
    
    # Making a post request 
    response = requests.post(url, data=payload)

    # Convert json into dictionary 
    respJson = response.json()

    # print response status code
    print("\nResponse Status Codes: ", response.status_code)

    # Pretty Printing JSON string back 
    print("Response Body:\n", json.dumps(respJson, indent=4, sort_keys=True))

    # assert
    assert response.status_code == 200
    assert respJson.get("id") == 4

    validate(instance=respJson, schema=jsonSchema)
    # No error, the JSON is valid.