from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health/live")

    assert response.status_code == 503
    assert response.get_json() == {"status": "ok"}
