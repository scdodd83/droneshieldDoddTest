import os
from creds import api_user, api_pass
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

def test_user_login(api_request_context: APIRequestContext) -> None:

    url = "	https://petstore.swagger.io/v2/user/login?"
    
    response = api_request_context.get(url, data = {"username": api_user, "password": api_pass})

    # Check for success response
    assert response.status == 200

def test_user_logout(api_request_context: APIRequestContext) -> None:

    url = "	https://petstore.swagger.io/v2/user/logout"

    response = api_request_context.get(url)

    # Check for success response
    assert response.status == 200

