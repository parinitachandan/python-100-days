import requests

MY_LAT = 12.971599
MY_LNG = 77.594566
location = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0  # when data is formatted(i.e = 0), it is in 12-hour format time; 1 is default
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=location, )
data = response.json()
print(data)

print("")

sunrise = data["results"]["sunrise"]
print(sunrise)
print(sunrise.split("T")[1].split(":"))



