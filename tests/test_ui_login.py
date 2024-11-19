import re
import creds
from playwright.sync_api import Page, expect, sync_playwright

def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title(re.compile("Swag Labs"))

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