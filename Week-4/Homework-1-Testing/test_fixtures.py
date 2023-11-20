import json
from fastapi.testclient import TestClient
import pytest
from main import app

@pytest.fixture
def good_payload():
    return {
        "name": "unit testing",
        "author": {"name": "John Jacob Hingleminer", "author_id": "SEAN-1999"},
        "year_published": 1955,
    }


@pytest.fixture
def bad_payload():
    return {
        "name": 12,
        "author": {"name": "John jacob Hingleminer", "author_id": "SEAN-SEAN"},
        "year_published": 1955,
    }


@pytest.fixture
def client():
  yield TestClient(app)
  
@pytest.mark.parametrize("payload, http_codes",
                           [
                             ("good_payload",200),
                             ("bad_payload",422)
                           ],)
def test_put_params(payload, http_codes, client, request ):
    assert client.put("/books/unit_test", json=request.getfixturevalue(payload)).status_code == http_codes
    pass
  
@pytest.mark.parametrize("file_path, http_codes", 
                         [
                           ("unit_test",200),
                           ("unit_test1",404)
                         ],)
def test_get_params(file_path, http_codes, client, good_payload):
  put_response = client.put("/books/unit_test", json=good_payload)
  assert put_response.status_code == 200
  get_response = client.get("/books/"+ file_path)
  assert get_response.status_code == http_codes
  assert good_payload == json.loads(get_response._content)
  pass