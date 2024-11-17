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
        base_url="https://petstore.swagger.io/v2", extra_http_headers=headers
    )
    yield request_context
    request_context.dispose()

def test_post_new_pet_ok(api_request_context: APIRequestContext) -> None:
    data = {
      "id": 77002,
      "category": {
        "id": 0,
        "name": "Pippin"
      },
      "name": "doggie",
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

    new_pet = api_request_context.post(
        f"/pet", data=data
    )
    api_request_context.post("https://petstore.swagger.io/v2/pet").ok