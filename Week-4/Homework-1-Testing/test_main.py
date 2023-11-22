#pytest
import json
from fastapi.testclient import TestClient
from main import app
import sqlmodel from pydantic

client = TestClient(app)

test_json = {
        "name": "unit testing",
        "author": {
            "name": "John Jacob Hingleminer",
            "author_id": "SEAN-1999"
        },
        "year_published": 1955
    }

bad_test_json = {
        "name": 12,
        "author": {
            "name": "John jacob Hingleminer",
            "author_id": "SEAN-SEAN"
        },
        "year_published": 1955
    }


def test_basic_exaple():
  assert(True)

def test_good_put_request():
  put_response = client.put("/books/unit_test", json=test_json)
  assert put_response.status_code == 200
  get_response = client.get("/books/unit_test")
  assert get_response.status_code == 200
  assert test_json == json.loads(get_response._content)

def test_bad_put_request():
  put_response = client.put("/books/unit_test", json=bad_test_json)
  assert put_response.status_code == 422

def test_delete_request():
  test_good_put_request()
  delete_response = client.delete("/books/unit_test")
  assert delete_response.status_code == 200
  get_response = client.get("/books/unit_test")
  assert get_response.status_code == 404

def test_get_all_request():
  get_response = client.get("/books/")
  assert get_response.status_code == 200
  first_response_length = len(get_response._content)
  client.put("/books/unit_test", json=test_json)
  get_response = client.get("/books/")
  second_response_length = len(get_response._content)
  assert first_response_length < second_response_length
  
  
  