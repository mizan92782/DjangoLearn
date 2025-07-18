import requests

URL = "http://127.0.0.1:8000/students/"

def GET():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.ConnectionError:
        print("❌ Failed to connect to the server. Is Django running?")
    except requests.exceptions.RequestException as e:
        print(f"❌ Some error occurred: {e}")

GET()
