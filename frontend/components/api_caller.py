import requests
import time
from config.settings import API_BASE_URL

def fetch_api(endpoint):
    ''' Sends a GET request to the specified API endpoint and returns:
     - response data (if successful)
     - execution time
     - error message (if any)'''
    
    start_time = time.time()
    try:
        response = requests.get(f"{API_BASE_URL}{endpoint}")
        response.raise_for_status()  # Raise an exception for non-2xx responses
        end_time = time.time()
        execution_time = end_time - start_time
        return response.json(), execution_time, None
    except requests.RequestException as e:
        end_time = time.time()
        execution_time = end_time - start_time
        return None, execution_time, str(e)
