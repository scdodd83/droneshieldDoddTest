import re
import creds
from playwright.sync_api import Page, expect, sync_playwright

def test_cart(page: Page):
    page.goto("https://www.saucedemo.com/")

# Login:    

    # Enter username.
    page.get_by_placeholder("Username").click()
    page.locator("#user-name").fill(creds.username)

    # Enter password.
    page.get_by_placeholder("Password").click()
    page.locator("#password").fill(creds.password)

    # Click login button.
    page.locator("#login-button").click()

    # Expects page to have a heading with the name Swag Labs.
    expect(page.locator(".app_logo")).to_be_visible()

# Main page:

    # Add items to cart.
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    expect(page.locator(".shopping_cart_badge")).to_contain_text("1")

    # Add another item to the cart.
    page.locator("#add-to-cart-sauce-labs-bike-light").click()
    expect(page.locator(".shopping_cart_badge")).to_contain_text("2")

    # Add all items to cart.
    page.locator("#add-to-cart-sauce-labs-bolt-t-shirt").click()
    page.locator("#add-to-cart-sauce-labs-fleece-jacket").click()
    page.locator("#add-to-cart-sauce-labs-onesie").click()
    page.locator("#add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)").click()
    expect(page.locator(".shopping_cart_badge")).to_contain_text("6")

# Cart:

    # Navigate to cart.
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".title")).to_have_text("Your Cart")

    # Continue shopping.
    page.locator("#continue-shopping").click()
    expect(page.locator(".app_logo")).to_be_visible()

    # Navigate back to cart.
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".title")).to_have_text("Your Cart")

    # Navigate to item details page from cart.
    page.locator("#item_4_title_link > div:nth-child(1)").click()
    expect(page.locator(".inventory_details_name")).to_have_text("Sauce Labs Backpack")

    # Navigate back to cart.
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".title")).to_have_text("Your Cart")

    # Remove the red shirt.
    page.locator("#remove-test\\.allthethings\\(\\)-t-shirt-\\(red\\)").click()
    # expect(page.locator(".cart_list")).to_have_class("removed_cart_item")

    # Checkout button.
    page.locator("#checkout").click()
    expect(page.locator(".title")).to_have_text("Checkout: Your Information")