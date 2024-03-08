import requests
from Lita.headers_urls import BASE_URL

class DataFetcher:
    def __init__(self, endpoint):
        self.url = BASE_URL + endpoint

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                json_data = response.json()
                # Check the status field in the JSON response
                if 'status' in json_data and json_data['status'] == '1':
                    status_code = 400  # Set status code to 400 if status is '1'
                else:
                    status_code = response.status_code
                return json_data, status_code
            else:
                return response.json(), response.status_code
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, None

class DataManager:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        # Your data processing logic goes here
        # Example: extracting relevant information, formatting, etc.
        pass
