import re
from playwright.sync_api import Page, expect

def test_left_nav(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Enter username.
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("standard_user")

    # Enter password.
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("secret_sauce")

    # Click login button.
    page.locator("#login-button").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.locator(".app_logo")).to_be_visible()

    # Expand the left nav.
    page.locator("#react-burger-menu-btn").click()
    expect(page.locator("#inventory_sidebar_link")).to_be_visible()

    # Collapse the left nav.
    page.locator("#react-burger-cross-btn").click()
    expect(page.locator(".title")).to_be_visible()