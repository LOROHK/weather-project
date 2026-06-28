import requests

# === AFYANALYTICS CREDENTIALS ===
BASE_URL = "https://staging.collabmed.net/api/external"
PLATFORM_NAME = "Test Platform v2"
PLATFORM_KEY = "afya_2d00d74512953c933172ab924f5073fa"
PLATFORM_SECRET = "e0502a5c052842cf19d0305455437b791d201761c88e2ad641680b2d5d356ba8"
CALLBACK_URL = "https://your-platform-url/callback"

# === STEP 1: INITIATE HANDSHAKE ===
def initiate_handshake():
    url = f"{BASE_URL}/initiate-handshake"
    payload = {
        "platform_name": PLATFORM_NAME,
        "platform_key": PLATFORM_KEY,
        "platform_secret": PLATFORM_SECRET,
        "callback_url": CALLBACK_URL
    }
    print("Step 1: Initiating handshake...")
    response = requests.post(url, json=payload)
    data = response.json()
    print("Status code:", response.status_code)
    print("Response:", data)
    try:
        token = data["data"]["handshake_token"]
        expires = data["data"]["expires_at"]
        print(f"Handshake token received. Expires at: {expires}")
        return token
    except KeyError:
        print("Failed to get handshake token:", data)
        return None

# === STEP 2: COMPLETE HANDSHAKE ===
def complete_handshake(handshake_token):
    url = f"{BASE_URL}/complete-handshake"
    payload = {
        "handshake_token": handshake_token,
        "platform_key": PLATFORM_KEY
    }
    print("\nStep 2: Completing handshake...")
    response = requests.post(url, json=payload)
    data = response.json()
    print("Status code:", response.status_code)
    print("Response:", data)
    try:
        access_token = data["data"]["access_token"]
        print("Access token received - handshake complete!")
        return access_token
    except KeyError:
        print("Failed to complete handshake:", data)
        return None

# === MAIN FLOW ===
handshake_token = initiate_handshake()

if handshake_token:
    access_token = complete_handshake(handshake_token)
    if access_token:
        print("\nAuthentication successful - ready to use Afyanalytics API")
    else:
        print("\nHandshake failed at step 2")
else:
    print("\nHandshake failed at step 1")