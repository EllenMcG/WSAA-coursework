import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"
response = requests.get(url)

if response.status_code == 200: # Check if the request was successful
    # Parse the JSON response
    data = response.json()
    
    # Save the data to a file called "cso.json"
    with open("cso.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("Dataset successfully saved to 'cso.json'.")
else:
    print(f"Failed to retrieve dataset. HTTP Status Code: {response.status_code}")