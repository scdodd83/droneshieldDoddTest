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

def test_add_pet(api_request_context: APIRequestContext) -> None:
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

    assert response.status == 200, f"Unexpected Status"    

def test_get_pet_by_id(api_request_context: APIRequestContext) -> None:

    url = "	https://petstore.swagger.io/v2/pet/77002"
    
    response = api_request_context.get(url)

    # Check for success response
    assert response.status == 200