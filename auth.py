import requests

url = "https://dummyjson.com/auth/login"

credentials = {
    "username": "emilys",
    "password": "emilyspass"
}

response = requests.post(url, json=credentials)
data = response.json()

print("Status code:", response.status_code)
print("Token:", data.get("accessToken"))
token = data.get("accessToken")

headers = {
    "Authorization": f"Bearer {token}"
}

protected = requests.get("https://dummyjson.com/auth/me", headers=headers)
print("Protected data:", protected.json())