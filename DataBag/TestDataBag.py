import json

class TestData:


    token_id = "1a01990ee079fc0733bdc253a92ca16313d41428f268be5010ce9337d0df83d9"

    def endpoint_method(self):
        endpoint_file = open("D:\\RestAPI_Project1\\Test_endpoints\\endpoint.json", "r").read()
        end_dict = json.loads(endpoint_file)
        url = end_dict['endpoint']
        return url


    def payload_method(self):
        payload_file = open("D:\\RestAPI_Project1\\Test_Payload\\payload_request.json", "r").read()
        payload = json.loads(payload_file)
        return payload


    def header_method(self):
        header_file = open("D:\\RestAPI_Project1\\Test_endpoints\\header_file.json", "r").read()
        header = json.loads(header_file)
        return header




