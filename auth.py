import requests

BASE_URL = "https://regions-test.2gis.com"

def get_auth_token():
    """Получение сессионного токена"""
    response = requests.post(f"{BASE_URL}/v1/auth/tokens")
    return response.cookies.get("token")
