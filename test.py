import requests

BASE_URL = 'http://localhost:5000'

def test_auth_register():
    response = requests.post(
        url = f'{BASE_URL}/auth/register', 
        json = {
            'username': 'john_doe_001',
            'password': 'john_doe_001',
            'name': 'John Doe 001',
            'email': 'john.doe.001@unmail.com',
            'phone_number': '081234567890'
        }, 
        headers = {
            'Content-Type': 'application/json'
        }
    )
    print(response.json())

def test_auth_login():
    response = requests.post(
        url = f'{BASE_URL}/auth/login', 
        json = {
            'username': 'john_doe_001',
            'password': 'john_doe_001'
        }, 
        headers = {
            'Content-Type': 'application/json'
        }
    )
    print(response.json())

if __name__ == '__main__':
    test_auth_login()