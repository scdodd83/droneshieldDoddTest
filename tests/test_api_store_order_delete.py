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

def test_add_order(api_request_context: APIRequestContext) -> None:
    data = {
        "id": 12345,
        "petId": 77002,
        "quantity": 1,
        "shipDate": "2024-11-18T21:48:15.165Z",
        "status": "placed",
        "complete": True
        }

    post_order = api_request_context.post(f"store/order", data=data)

    # Check for success response
    assert post_order.status == 200

def test_delete_order(api_request_context: APIRequestContext) -> None:

    url = "https://petstore.swagger.io/v2/store/order/12345"

    response = api_request_context.delete(url)
    
    # Check for success response
    assert response.status == 200