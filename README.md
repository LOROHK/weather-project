# Afyanalytics Platform Integration

A Python-based integration with the Afyanalytics Health Platform, implementing 
a secure two-step handshake authentication flow.

## Setup Instructions

1. Clone this repository:
   git clone https://github.com/LOROHK/weather-project.git

2. Install dependencies:
   pip install requests

3. Add your platform credentials in handshake.py:
   PLATFORM_NAME = "your platform name"
   PLATFORM_KEY = "your platform key"
   PLATFORM_SECRET = "your platform secret"

4. Run the handshake:
   python3 handshake.py

## How the Handshake Flow Works

Step 1 - Initiate Handshake:
- Sends platform credentials to /initiate-handshake
- Receives a handshake token valid for 15 minutes

Step 2 - Complete Handshake:
- Sends handshake token to /complete-handshake
- Receives access token and refresh token for API access

## How Token Expiry is Handled

- Handshake token expires in 15 minutes
- If token expires, the script detects failure and prompts re-initiation
- Access token expires in 6 hours
- Error handling catches expired or invalid tokens gracefully

## Project Structure

- handshake.py — Afyanalytics two-step handshake implementation
- auth.py — Practice authentication with JWT tokens
- weather.py — Weather API integration (single city)
- test_loop.py — Weather API integration (multiple cities with loops)