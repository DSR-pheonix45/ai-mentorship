import requests

class HuggingFaceAPIClient:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://api-inference.huggingface.co/models/"

    def query_model(self, model_name, payload):
        headers = {"Authorization": f"Bearer {self.api_token}"}
        response = requests.post(self.base_url + model_name, headers=headers, json=payload)
        return response.json()