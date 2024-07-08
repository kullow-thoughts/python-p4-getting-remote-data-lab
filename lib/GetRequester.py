import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_list = []
        json_responses = json.loads(self.get_response_body())
        for json_response in json_responses:
            response_list.append(json_response)
        return response_list