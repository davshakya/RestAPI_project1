import json
import requests
from DataBag.TestDataBag import TestData
import allure

@allure.description("create_user_with_valid_values")
@allure.severity(severity_level="Critical")
def test_create_user_with_valid_values_001():
    endpoint = TestData().endpoint_method()
    payload = TestData().payload_method()
    header = TestData().header_method()

    payload['name']='ramverma'
    payload['email']='rameverma@gmail.com'
    payload['gender']='male'
    payload['status']='active'

    payload_json = json.dumps(payload)
    response = requests.request("POST", endpoint, headers=header, data=payload_json)
    res_dict=response.json()
    print(res_dict)
    response_code = response.status_code
    assert response_code == 201
    
@allure.description("create_user_with_invalid_values")
@allure.severity(severity_level="Critical")
def test_create_user_with_invalid_values_002():
    endpoint = TestData().endpoint_method()
    payload = TestData().payload_method()
    header = TestData().header_method()

    payload['name']=''
    payload['email']='davshakya@gmail.com'
    payload['gender']='tiger'
    payload['status']=''

    payload_json = json.dumps(payload)
    response = requests.request("POST", endpoint, headers=header, data=payload_json)
    res_dict=response.json()
    massage=res_dict[0]['message']
    assert massage == "can't be blank"
    response_code = response.status_code
    assert response_code == 422

