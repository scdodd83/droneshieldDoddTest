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

def test_update_pet(api_request_context: APIRequestContext) -> None:
    data = {
        "id": 77002,
        "category": {
            "id": 0,
            "name": "best doggos"
        },
        "name": "Pippin",
        "photoUrls": [
            "shttps://d.newsweek.com/en/full/1979380/dog-running-through-autumn-leaves.webp"
        ],
        "tags": [
            {
            "id": 0,
            "name": "string"
            }
        ],
        "status": "available"
        }
    
    update_pet = api_request_context.put(
        f"pet", data=data
    )

    # Check for success response
    response_data = update_pet.json()
    assert update_pet.status == 200
    assert "photoUrls" in response_data, "string"