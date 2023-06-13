import requests

url = "https://date.nager.at/api/v3/CountryInfo/FR"

payload = {}
headers = {
  'accept': 'text/plain'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)