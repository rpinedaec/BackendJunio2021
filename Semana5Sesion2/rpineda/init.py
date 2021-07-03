import requests

url = "https://api-football-beta.p.rapidapi.com/countries"

headers = {
    'x-rapidapi-key': "1CIFo95k8NmshGrZw6jhJgFBVcxjp1km7hojsnFzYUhzUKSWPE",
    'x-rapidapi-host': "api-football-beta.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)