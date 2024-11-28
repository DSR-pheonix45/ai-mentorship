import time
from api_client import HuggingFaceAPIClient

class MentorshipModel:
    def __init__(self, api_token, model_name='gpt2'):
        self.api_client = HuggingFaceAPIClient(api_token)
        self.model_name = model_name

    def generate_response(self, prompt, max_length=100, max_retries=3, retry_delay=5):
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_length": max_length,
                "num_return_sequences": 1
            }
        }
        
        retries = 0
        while retries < max_retries:
            response = self.api_client.query_model(self.model_name, payload)
            
            # Check if the response is a list and contains the expected structure
            if isinstance(response, list) and len(response) > 0 and 'generated_text' in response[0]:
                return response[0]['generated_text']
            elif 'error' in response and 'estimated_time' in response:
                # Model is loading, wait and retry
                estimated_time = response['estimated_time']
                print(f"Model is loading. Retrying in {estimated_time} seconds...")
                time.sleep(estimated_time)
                retries += 1
            else:
                raise ValueError(f"Unexpected API response structure: {response}")
        
        raise ValueError("Failed to get a valid response after multiple retries.")