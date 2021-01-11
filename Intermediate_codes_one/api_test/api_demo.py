import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

print(response.status_code)
response.raise_for_status()
print(response.json())
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
location = (longitude, latitude)
print(location)
