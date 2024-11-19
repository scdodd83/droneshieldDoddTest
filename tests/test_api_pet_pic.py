import os
import requests
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

def test_post_pet_pic() -> None:

    url = "https://petstore.swagger.io/v2/pet/uploadFile"
    file_path = "docs/smallPic.jpg"

    with open(file_path, "rb") as image_file:
        files = {"image": image_file}
        response = requests.post(url, files=files)   

    # Check for success response
    assert response.status_code == 200