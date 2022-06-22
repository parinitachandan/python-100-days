import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

print(response.status_code)

print(response.raise_for_status())

print(response.url)

data = response.json()
print(data)

# accessing a key
latitude = data["iss_position"]["latitude"]
print(latitude)

longitude = data["iss_position"]["longitude"]
print(longitude)

# creating a tuple
iss_position = (longitude,latitude)
print(iss_position)
