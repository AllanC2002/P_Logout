import requests

BASE_URL = "http://3.90.92.74:8080" 

# 1. Login
login_payload = {
    "User_mail": "allan",  
    "password": "1234"           
}

login_response = requests.post(f"http://52.203.72.116:8080/login", json=login_payload)

if login_response.status_code == 200:
    token = login_response.json().get("token")
    print("Token:",token)
else:
    print("Error to login:", login_response.status_code, login_response.text)
    exit()

# 2. Logout
headers = {"Authorization": f"Bearer {token}"}
logout_response = requests.post(f"{BASE_URL}/logout", headers=headers)

print("\nLogout:")
print(logout_response.status_code, logout_response.json())

