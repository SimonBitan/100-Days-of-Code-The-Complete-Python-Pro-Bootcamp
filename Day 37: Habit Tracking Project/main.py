import requests
from datetime import datetime

USERNAME = "sijobi"
TOKEN = "guih388h&BYfgg8f68"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

post_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "12"
}

# response = requests.put(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(response.text)

put_pixel_endpoint = f"{post_pixel_endpoint}/20240423"

put_pixel_config = {
    "quantity": "25",
}

# response = requests.put(url=put_pixel_endpoint, json=put_pixel_config, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

response = requests.delete(delete_pixel_endpoint, headers=headers)
print(response.text)



