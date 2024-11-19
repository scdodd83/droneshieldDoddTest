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

def test_add_user_fail(api_request_context: APIRequestContext) -> None:
    data = {
        "id": 0,
        "username": "string",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
        }

    new_user = api_request_context.post(
        f"user/createUser", data=data
    )

    # Check for success response
    assert new_user.status == 405

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
    
    # response_data = response.json()       
    # assert response_data["id"] == data["id"], f"Incorrect 'id' in response: {response_data.get('id')}"
    # assert response_data["username"] == data["username"], f"Incorrect 'username' in response: {response_data.get('username')}"
    # assert response_data["firstName"] == data["firstName"], f"Incorrect 'firstName' in response: {response_data.get('firstName')}"
    # assert response_data["lastName"] == data["lastName"], f"Incorrect 'lastName' in response: {response_data.get('lastName')}"
    # assert response_data["email"] == data["email"], f"Incorrect 'email' in response: {response_data.get('email')}"
    # assert response_data["password"] == data["password"], f"Incorrect 'password' in response: {response_data.get('password')}"
    # assert response_data["phone"] == data["phone"], f"Incorrect 'phone' in response: {response_data.get('phone')}"
    # assert response_data["userStatus"] == data["userStatus"], f"Incorrect 'userStatus' in response: {response_data.get('userStatus')}"