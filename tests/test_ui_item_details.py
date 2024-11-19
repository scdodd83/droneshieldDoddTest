import re
import creds
from playwright.sync_api import Page, expect, sync_playwright

def test_item_details(page: Page):
    page.goto("https://www.saucedemo.com/")

# Login:    

    # Enter username.
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill(creds.username)

    # Enter password.
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(creds.password)

    # Click login button.
    page.locator("#login-button").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.locator(".app_logo")).to_be_visible()

# Main Page:

    # Select an item.
    page.locator("#item_4_title_link > div:nth-child(1)").click()
    expect(page.locator(".inventory_details_name")).to_have_text("Sauce Labs Backpack")

    # Back to products button functionality.
    page.locator("#back-to-products").click()
    expect(page.locator(".app_logo")).to_have_text("Swag Labs")

    # Select second item.
    page.locator("#item_0_title_link > div:nth-child(1)").click()
    expect(page.locator(".inventory_details_name")).to_have_text("Sauce Labs Bike Light")

    # Add to cart.
    page.locator("#add-to-cart").click()
    expect(page.locator("#remove")).to_contain_text("Remove")
    expect(page.locator(".shopping_cart_badge")).to_contain_text("1")

    # Remove from cart.
    page.locator("#remove").click()
    expect(page.locator("#add-to-cart")).to_contain_text("Add to cart")
    expect(page.locator("#shopping_cart_container")).to_be_visible()