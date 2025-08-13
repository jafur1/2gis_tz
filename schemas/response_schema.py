RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string", "minLength": 1, "maxLength": 999},
        "lat": {"type": "number"},
        "lon": {"type": "number"},
        "color": {"type": ["string", "null"]},
        "created_at": {"type": "string", "format": "date-time"}
    },
    "required": ["id", "title", "lat", "lon", "color", "created_at"],
    "additionalProperties": False
}
