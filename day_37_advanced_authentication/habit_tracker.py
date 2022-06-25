import requests
from datetime import datetime

USER_NAME = "parinita"
TOKEN = "hello1234!"
GRAPH_ID = "cyclegraph"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# user created
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating graph
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

token_header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=token_header)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? ")
}

data = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=token_header)
print(data.text)

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# put_response = requests.put(url=update_endpoint, json=new_pixel_data, headers=token_header)
# print(put_response.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


# delete = requests.delete(url=delete_endpoint, headers=token_header)
# print(delete.text)
