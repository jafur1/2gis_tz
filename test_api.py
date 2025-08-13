import uuid
import pytest
from jsonschema import validate
from datetime import datetime
from auth import get_auth_token
from schemas.response_schema import RESPONSE_SCHEMA
from api.favorites import create_favorite_place

class TestFavoritePlaces:
    def setup_method(self):
        self.token = get_auth_token()
        assert self.token is not None, "Не удалось получить токен"

    def test_creating_place_with_color(self):
        test_data = {
            "title": "Test Place",
            "lat": 55.028254,
            "lon": 82.918501,
            "color": "RED"}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        response_json = response.json()
        validate(instance=response_json, schema=RESPONSE_SCHEMA)
        assert response_json["title"] == test_data["title"]
        assert response_json["lat"] == test_data["lat"]
        assert response_json["lon"] == test_data["lon"]
        assert response_json["color"] == test_data["color"]
        try:
            datetime.fromisoformat(response_json["created_at"])
        except ValueError:
            pytest.fail("Поле created_at содержит невалидную дату")
        assert isinstance(response_json["id"], int) and response_json["id"] > 0

    def test_creating_place_not_color(self):
        test_data = {
            "title": "Test Place",
            "lat": 55.028254,
            "lon": 82.918501}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        response_json = response.json()
        validate(instance=response_json, schema=RESPONSE_SCHEMA)
        assert response_json["title"] == test_data["title"]
        assert response_json["lat"] == test_data["lat"]
        assert response_json["lon"] == test_data["lon"]
        try:
            datetime.fromisoformat(response_json["created_at"])
        except ValueError:
            pytest.fail("Поле created_at содержит невалидную дату")
        assert isinstance(response_json["id"], int) and response_json["id"] > 0

    def test_creating_place_with_border_top_and_bottom_with_color(self):
        test_data = {
            "title": "Test тесТ",
            "lat": 0,
            "lon": -180,
            "color": "BLUE"}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        response_json = response.json()
        validate(instance=response_json, schema=RESPONSE_SCHEMA)
        assert response_json["title"] == test_data["title"]
        assert response_json["lat"] == test_data["lat"]
        assert response_json["lon"] == test_data["lon"]
        assert response_json["color"] == test_data["color"]
        try:
            datetime.fromisoformat(response_json["created_at"])
        except ValueError:
            pytest.fail("Поле created_at содержит невалидную дату")
        assert isinstance(response_json["id"], int) and response_json["id"] > 0

    def test_creating_place_with_border_bottom_and_top_with_color(self):
        test_data = {
            "title": "Test тесТ",
            "lat": 90,
            "lon": 0,
            "color": "GREEN"}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
        response_json = response.json()
        validate(instance=response_json, schema=RESPONSE_SCHEMA)
        assert response_json["title"] == test_data["title"]
        assert response_json["lat"] == test_data["lat"]
        assert response_json["lon"] == test_data["lon"]
        assert response_json["color"] == test_data["color"]
        try:
            datetime.fromisoformat(response_json["created_at"])
        except ValueError:
            pytest.fail("Поле created_at содержит невалидную дату")
        assert isinstance(response_json["id"], int) and response_json["id"] > 0

    def test_create_favorite_place_with_null_color(self):
        test_data = {
            "title": "Test Place",
            "lat": 55.028254,
            "lon": 82.918501,
            "color": "Null"}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 400, f"Ожидалась ошибка 400, получен {response.status_code}"
        error_response = response.json()
        assert "error" in error_response
        assert "id" in error_response["error"]
        assert "message" in error_response["error"]
        try:
            uuid.UUID(error_response["error"]["id"])
        except ValueError:
            pytest.fail("ID ошибки не является валидным UUID")
        expected_message = "Параметр 'color' может быть одним из следующих значений: BLUE, GREEN, RED, YELLOW"
        assert error_response["error"]["message"] == expected_message

    def test_error_output_when_lat_is_greater_than_limit(self):
        test_data = {
            "title": "Test Place",
            "lat": 91,
            "lon": 82.918501}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 400, f"Ожидалась ошибка 400, получен {response.status_code}"
        error_response = response.json()
        assert "error" in error_response
        assert "id" in error_response["error"]
        assert "message" in error_response["error"]
        try:
            uuid.UUID(error_response["error"]["id"])
        except ValueError:
            pytest.fail("ID ошибки не является валидным UUID")
        expected_message = "Параметр 'lat' должен быть не более 90"
        assert error_response["error"]["message"] == expected_message

    def test_error_output_when_lat_is_less_than_limit(self):
        test_data = {
            "title": "Test Place",
            "lat": -91,
            "lon": 82.918501}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 400, f"Ожидалась ошибка 400, получен {response.status_code}"
        error_response = response.json()
        assert "error" in error_response
        assert "id" in error_response["error"]
        assert "message" in error_response["error"]
        try:
            uuid.UUID(error_response["error"]["id"])
        except ValueError:
            pytest.fail("ID ошибки не является валидным UUID")
        expected_message = "Параметр 'lat' должен быть не менее -90"
        assert error_response["error"]["message"] == expected_message

    def test_error_output_with_an_empty_lat(self):
        test_data = {
            "title": "Test Place",
            "lat": " ",
            "lon": 82.918501}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 400, f"Ожидалась ошибка 400, получен {response.status_code}"
        error_response = response.json()
        assert "error" in error_response
        assert "id" in error_response["error"]
        assert "message" in error_response["error"]
        try:
            uuid.UUID(error_response["error"]["id"])
        except ValueError:
            pytest.fail("ID ошибки не является валидным UUID")
        expected_message = "Параметр 'lat' должен быть числом"
        assert error_response["error"]["message"] == expected_message

    def test_error_output_when_lon_is_greater_than_limit(self):
        test_data = {
            "title": "Test Place",
            "lat": 23,
            "lon": 181}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 400, f"Ожидалась ошибка 400, получен {response.status_code}"
        error_response = response.json()
        assert "error" in error_response
        assert "id" in error_response["error"]
        assert "message" in error_response["error"]
        try:
            uuid.UUID(error_response["error"]["id"])
        except ValueError:
            pytest.fail("ID ошибки не является валидным UUID")
        expected_message = "Параметр 'lon' должен быть не более 180"
        assert error_response["error"]["message"] == expected_message

    def test_error_output_when_lon_is_less_than_limit(self):
        test_data = {
            "title": "Test Place",
            "lat": 23,
            "lon": -181}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 400, f"Ожидалась ошибка 400, получен {response.status_code}"
        error_response = response.json()
        assert "error" in error_response
        assert "id" in error_response["error"]
        assert "message" in error_response["error"]
        try:
            uuid.UUID(error_response["error"]["id"])
        except ValueError:
            pytest.fail("ID ошибки не является валидным UUID")
        expected_message = "Параметр 'lon' должен быть не менее -180"
        assert error_response["error"]["message"] == expected_message

    def test_error_output_with_an_empty_lon(self):
        test_data = {
            "title": "Test Place",
            "lat": 34,
            "lon": " "}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 400, f"Ожидалась ошибка 400, получен {response.status_code}"
        error_response = response.json()
        assert "error" in error_response
        assert "id" in error_response["error"]
        assert "message" in error_response["error"]
        try:
            uuid.UUID(error_response["error"]["id"])
        except ValueError:
            pytest.fail("ID ошибки не является валидным UUID")
        expected_message = "Параметр 'lon' должен быть числом"
        assert error_response["error"]["message"] == expected_message

    def test_error_output_with_an_empty_title(self):
        test_data = {
            "title": "",
            "lat": 34,
            "lon": 43}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 400, f"Ожидалась ошибка 400, получен {response.status_code}"
        error_response = response.json()
        assert "error" in error_response
        assert "id" in error_response["error"]
        assert "message" in error_response["error"]
        try:
            uuid.UUID(error_response["error"]["id"])
        except ValueError:
            pytest.fail("ID ошибки не является валидным UUID")
        expected_message = "Параметр 'title' не может быть пустым"
        assert error_response["error"]["message"] == expected_message

    def test_error_output_when_title_is_greater_than_limit(self):
        test_data = { #В title 1000 символов
            "title": 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,
            "lat": 55.028254,
            "lon": 82.918501,
            "color": "RED"}
        response = create_favorite_place(self.token, **test_data)
        assert response.status_code == 400, f"Ожидалась ошибка 400, получен {response.status_code}"
        error_response = response.json()
        assert "error" in error_response
        assert "id" in error_response["error"]
        assert "message" in error_response["error"]
        try:
            uuid.UUID(error_response["error"]["id"])
        except ValueError:
            pytest.fail("ID ошибки не является валидным UUID")
        expected_message = "Параметр 'title' должен содержать не более 999 символов"
        assert error_response["error"]["message"] == expected_message