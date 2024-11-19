import os
import requests
import json
import base64
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

def test_post_pet_pic() -> None:

    url = "https://petstore.swagger.io/v2/pet/77002/uploadImage"
    file_path = "docs/smallPic.jpg"

    with open(file_path, "rb") as image_file:
        files = {"image": image_file}
        response = requests.post(url, files=files)   

    # Check for success response
    assert response.status_code == 200