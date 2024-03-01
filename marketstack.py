
import os
import requests
import json

API_KEY = os.environ.get("MARKETSTACK_KEY")
BASE_URL = 'http://api.marketstack.com/v1/'

def get_stock_price(stock_symbol):
    params = {
        'access_key': API_KEY
    }
    endpoint = ''.join([BASE_URL, "tickers/", stock_symbol, "/intraday/latest"])
    
    try:
        api_result = requests.get(endpoint, params=params)
        api_result.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        json_result = api_result.json()
        
        # Check if the key "last" exists in the JSON response
        if 'last' in json_result:
            last_price = json_result['last']
            return {"last_price": last_price}
        else:
            print("Key 'last' not found in API response.")
            return None
        
    except Exception as e:
        print(f"Error retrieving stock price: {e}")
        return None
