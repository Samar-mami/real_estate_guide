import requests
import pandas as pd

url = "https://seloger.p.rapidapi.com/locations/search"

querystring = {"searchTerm": "paris"}

headers = {
    "X-RapidAPI-Key": "4462bef6d9mshffa2af5b3dd7219p193e1cjsn625dfb1b6d9c",
    "X-RapidAPI-Host": "seloger.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring, verify=False)
response_json = response.json()
df = pd.DataFrame(response_json)
print(df.head())