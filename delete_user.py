# import required modules
import requests

# Set the base url
BASE_URL = "https://reqres.in"


def test_success_delete_user():
    url = BASE_URL + "/api/users/"

    path_params = "2"

    # Making a delete request
    response = requests.delete(url + path_params)

    print("\n------------Request------------")

    print("Method : ", response.request)
    print("Url : ", response.url)

    print("\n------------Response------------")

    # print response status code
    print("Response Status Codes: ", response.status_code, response.reason)

    # get response headers
    content_type = response.headers.get("Content-Type")

    # assert
    assert response.status_code == 204, "Unexpected status code: " + \
        str(response.status_code)
    
    # Asserting Response Headers
    assert content_type == None, "Unexpected Content-Type: " + str(content_type)

    # is empty response body
    assert len(response.text) == 0, "Unexpected Response Body Length " + \
        str(len(response.text))
    
    # check the substring in the response body
    assert bool("update" in response.text) == False
    assert bool("zion" in response.text) == False