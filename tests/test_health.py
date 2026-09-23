from app import app


def test_health():
    client = app.test_client()

    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_readiness_without_database_config(monkeypatch):
    monkeypatch.delenv("DB_HOST", raising=False)

    client = app.test_client()
    response = client.get("/health/ready")

    assert response.status_code == 503
    assert response.get_json() == {"status": "not ready"}