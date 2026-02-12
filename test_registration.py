import requests
import json

# Test the registration endpoint
url = "http://127.0.0.1:8000/auth/register"

# Test data
test_data = {
    "email": "test@example.com",
    "password": "testpassword123"
}

headers = {
    "Content-Type": "application/json"
}

try:
    print("Testing user registration...")
    response = requests.post(url, data=json.dumps(test_data), headers=headers)

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code == 201:
        print("Registration successful!")
    else:
        print("Registration failed!")

except requests.exceptions.ConnectionError:
    print("Cannot connect to the server. Please make sure the backend is running on http://127.0.0.1:8000")
except Exception as e:
    print(f"Error occurred: {str(e)}")