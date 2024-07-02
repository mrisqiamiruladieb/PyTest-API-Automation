# import required modules 
import requests
import json

def test_get_list_of_users():

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