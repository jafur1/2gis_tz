import requests
from auth import BASE_URL

def create_favorite_place(token, title, lat, lon, color=None):
    """Создание избранного места"""
    data = {
        "title": title,
        "lat": lat,
        "lon": lon}
    if color:
        data["color"] = color
    cookies = {"token": token}
    response = requests.post(
        f"{BASE_URL}/v1/favorites",
        data=data,
        cookies=cookies)
    return response
