import re
import creds
from playwright.sync_api import Page, expect, sync_playwright

def test_cart(page: Page):
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

    # Expects page to have a heading with the name Swag Labs.
    expect(page.locator(".app_logo")).to_be_visible()

# Main page:

    # Add items to cart.
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    expect(page.locator(".shopping_cart_badge")).to_contain_text("1")

    # Navigate to cart.
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".title")).to_have_text("Your Cart")

# Checkout:

    # Select checkout button.
    page.locator("#checkout").click()
    expect(page.locator(".title")).to_have_text("Checkout: Your Information")  

    # Continue without filling in information.
    page.locator("#continue").click()
    expect(page.locator(".error-message-container > h3:nth-child(1)")).to_have_text("Error: First Name is required")

    # Fill in required fields.
    page.locator("#first-name").fill("Tester")
    page.locator("#last-name").fill("McTesterson")
    page.locator("#postal-code").fill("77002")
    
    # Select continue.
    page.locator("#continue").click()
    expect(page.locator(".title")).to_have_text("Checkout: Overview")

    # Select cancel.
    page.locator("#cancel").click()
    expect(page.locator(".title")).to_have_text("Products")

    # Navigate back to checkout.
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".title")).to_have_text("Your Cart")
    page.locator("#checkout").click()
    expect(page.locator(".title")).to_have_text("Checkout: Your Information")
    page.locator("#first-name").fill("Tester")
    page.locator("#last-name").fill("McTesterson")
    page.locator("#postal-code").fill("77002")
    page.locator("#continue").click()
    expect(page.locator(".title")).to_have_text("Checkout: Overview")

    # Complete transaction.
    page.locator("#finish").click()
    expect(page.locator(".title")).to_have_text("Checkout: Complete!")

    # Select back home button.
    page.locator("#back-to-products").click()
    expect(page.locator(".title")).to_have_text("Products")