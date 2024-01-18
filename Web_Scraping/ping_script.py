# ping_script.py
import requests

def ping_frontend():
    frontend_url = 'https://next-app-h2qh.onrender.com'
    response = requests.get(frontend_url)
    print(response)
    print(f'Frontend Ping Status Code: {response.status_code}')

def ping_backend():
    backend_url = 'https://backend-app-ygah.onrender.com/api/'
    response = requests.get(backend_url)
    print(response)
    print(f'Backend Ping Status Code: {response.status_code}')

def main():
    ping_frontend()
    ping_backend()

if __name__ == "__main__":
    main()
