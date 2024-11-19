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

def test_add_user_ok(api_request_context: APIRequestContext) -> None:
    data = {
        "id": 77002,
        "username": "tester42",
        "firstName": "Tester",
        "lastName": "McTesterson",
        "email": "testing@thisthinghere.com",
        "password": "terriblemethod",
        "phone": "1234567890",
        "userStatus": 0
        }

    response = api_request_context.post(f"user", data=data)

    # Check for success response
    assert response.status == 200     

def test_delete_user(api_request_context: APIRequestContext) -> None:

    url = "	https://petstore.swagger.io/v2/user/tester42"
    
    response = api_request_context.get(url)

    # Check for success response
    assert response.status == 200  