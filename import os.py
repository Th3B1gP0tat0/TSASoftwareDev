import os
import requests

API_KEY = 'Ninja1003^' 
BASE_URL = 'https://ei.api.palmetto.com/v1'


headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}


def get_energy_data(address):
    endpoint = f'{BASE_URL}/energy/carbon'
    payload = {'address': address}

    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        print("Energy Data:", data)
        return data
    else:  print("Error:", response.status_code, response.text)


sample_address = "10770 240th Ave NE, Redmond, WA 98053"
get_energy_data(sample_address)
try:
    response = requests.post(endpoint, headers=headers, json=payload, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Request failed:", e)