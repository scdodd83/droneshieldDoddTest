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

def test_get_store_inventory(api_request_context: APIRequestContext) -> None:
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
    
    # response_data = post_order.json()    
    # assert response_data["id"] == data["id"], f"Incorrect 'id' in response: {response_data.get('id')}"
    # assert response_data["petId"] == data["petId"], f"Incorrect 'name' in response: {response_data.get('petId')}"
    # assert response_data["quantity"] == data["quantity"], f"Incorrect 'quantity' in response: {response_data.get('quantity')}"
    # assert response_data["shipDate"] == data["shipDate"], f"Incorrect 'shipDate' in response: {response_data.get('shipDate')}"
    # assert response_data["status"] == data["status"], f"Incorrect 'status' in response: {response_data.get('status')}"
    # assert response_data["complete"] == data["complete"], f"Incorrect 'complete' in response: {response_data.get('complete')}"