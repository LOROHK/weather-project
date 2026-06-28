import requests

# === CONFIGURATION - swap these for real values ===
LOGIN_URL = "https://your-hospital-api.com/auth/login"
USERNAME = "your_username"
PASSWORD = "your_password"
# ==================================================

def get_token(username, password):
    credentials = {
        "username": username,
        "password": password
    }
    response = requests.post(LOGIN_URL, json=credentials)
    data = response.json()
    try:
        token = data["token"]  # adjust key name to match real API
        print("Token received successfully")
        return token
    except KeyError:
        print("Login failed:", data)
        return None

def get_protected_data(token, endpoint):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

# === MAIN FLOW ===
token = get_token(USERNAME, PASSWORD)

if token:
    print("Handshake complete - ready to make authenticated requests")
else:
    print("Handshake failed - check credentials")