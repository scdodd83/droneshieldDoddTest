import os
from typing import Generator
import pytest
from playwright.sync_api import Playwright, APIRequestContext

PETSTORE_API_TOKEN = os.getenv("special-key")

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
        "Authorization": f"token {PETSTORE_API_TOKEN}",
    }
    request_context = playwright.request.new_context(
        base_url="https://petstore.swagger.io/v2/", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()

def test_post_new_pet_fail(api_request_context: APIRequestContext) -> None:
    data = {
        "id": 77002,
      "category": {
        "id": 0,
        "name": 1
      },
      "name": 2,
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": 3
        }
      ],
      "status": "available"
    }

    new_pet = api_request_context.post(
        f"pet", data=data
    )

    assert new_pet.status == 405, f"Unexpected Status: {new_pet.status}"    

def test_post_new_pet_ok(api_request_context: APIRequestContext) -> None:
    data = {
      "id": 77002,
      "category": {
        "id": 0,
        "name": "Best Doggos"
      },
      "name": "Pippin",
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": "available"
    }

    response = api_request_context.post(f"pet", data=data)

    assert response.status == 200
    
    # response_data = response.json()    
    # assert response_data["id"] == data["id"], f"Incorrect 'id' in response: {response_data.get('id')}"
    # assert response_data["name"] == data["name"], f"Incorrect 'name' in response: {response_data.get('name')}"
    # assert response_data["status"] == data["status"], f"Incorrect 'status' in response: {response_data.get('status')}"
    # assert response_data["category"]["name"] == data["category"]["name"], f"Incorrect 'category.name' in response: {response_data['category'].get('name')}"
    # assert "photoUrls" in response_data, "Missing 'photoUrls' in response"