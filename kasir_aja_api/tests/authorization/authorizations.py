# import required modules
import requests
import json
from jsonschema import validate
import random

# Set the base url
BASE_URL = "https://kasir-api.belajarqa.com"

def test_success_register():

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
                    "name": {
                        "type": "string"
                    },
                    "email": {
                        "type": "string"
                    }
                },
                "required": [
                    "name",
                    "email"
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
        "name": "nama Toko " + str(rand_int),
        "email": "hello" + str(rand_int) + "@gmail.com",
        "password": "12345678" + str(rand_int),
    }

    # Making a post request
    response = requests.post(BASE_URL + "/registration", data=payload)

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

    # declare the global variables
    global email_request
    global password_request

    # Parse the request body
    email_request = payload.get('email')
    name_request = payload.get('name')
    password_request = payload.get('password')

    # Parse the response body
    email_response = respJson.get('data').get('email')
    name_response = respJson.get('data').get('name')

    # get response headers
    content_type = response.headers.get("Content-Type")

    # assert
    assert response.status_code == 201, "Unexpected status code: " + \
        str(response.status_code)
    assert email_response == email_request, "Unexpected email: " + email_request
    assert name_response == name_request, "Unexpected email: " + name_request

    # Asserting Response Headers
    assert content_type == "application/json; charset=utf-8", "Unexpected Content-Type: " + content_type

    # is empty response body
    assert len(string_resp_body) != 0, "Unexpected Response Body Length " + \
        str(len(string_resp_body))
    assert len(str(respJson.get("status"))) != 0, "Unexpected Response Body Length " + \
        str(len(str(respJson.get("status"))))

    # check the substring in the response body
    assert bool("berhasil" in string_resp_body) == True

    validate(instance=respJson, schema=jsonSchema)
    # No error, the JSON is valid.

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

    # declare the global variables
    global email_request
    global password_request
    global access_token_response
    global refresh_token_response

    payload = {
        "email": email_request,
        "password": password_request,
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
    print("Request Body :\n", json.dumps(payload, indent=4, sort_keys=False))

    print("\n------------Response------------")

    # print response status code
    print("Response Status Codes: ", response.status_code, response.reason)

    # Pretty Printing JSON string back
    print("Response Body:\n", json.dumps(respJson, indent=4, sort_keys=False))

    # Parse the request body
    email_request = payload.get('email')

    # Parse the response body
    email_response = respJson.get('data').get('user').get('email')
    access_token_response = respJson.get('data').get('accessToken')
    refresh_token_response = respJson.get('data').get('refreshToken')

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

    # declare the global variables
    global access_token_response
    global refresh_token_response

    payload = {
        "refreshToken": refresh_token_response
    }

    access_token = access_token_response

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
    print("Request Body :\n", json.dumps(payload, indent=4, sort_keys=False))

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

def test_success_logout():

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
            }
        },
        "required": [
            "status",
            "message"
        ]
    }

    # declare the global variables
    global refresh_token_response

    payload = {
        "refreshToken": refresh_token_response
    }

    # Making a delete request
    response = requests.delete(BASE_URL + "/authentications", json=payload)

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
    assert bool("Refresh token berhasil dihapus" in string_resp_body) == True

    validate(instance=respJson, schema=jsonSchema)
    # No error, the JSON is valid.