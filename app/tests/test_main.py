
from fastapi.testclient import TestClient
from starlette.responses import RedirectResponse
from app.main import app

client = TestClient(app)


def test_root_redirect():
    response = client.get("/")
    assert response.status_code == 200
    response = RedirectResponse('/api/v1')
    assert response
    assert response.status_code == 307


def test_root():
    response = client.get("/api/v1")
    assert response.status_code == 200
    assert response.json() == {
        "message": "use www.examplehost.com/docs for documentation regarding the API."}
