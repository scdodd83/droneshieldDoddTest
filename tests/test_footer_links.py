import re
from playwright.sync_api import Page, expect, sync_playwright

def test_footer_links(page: Page):
    page.goto("https://www.saucedemo.com/")

# Login:     

    # Enter username.
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill("standard_user")

    # Enter password.
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("secret_sauce")

    # Click login button.
    page.locator("#login-button").click()

# Footer Links:    

    # Expects page to have a heading with the name of Installation.
    expect(page.locator(".app_logo")).to_be_visible()

    # Selecting X (formerly twitter) link.
    page.locator(".social_twitter > a:nth-child(1)").click()
    # expect(page).to_have_url(re.compile("https://x.com/saucelabs"))

    page.wait_for_timeout(5000)

    # Selecting Facebook link.
    page.locator(".social_facebook > a:nth-child(1)").click()
    # expect(page).to_have_url(re.compile("https://www.facebook.com/saucelabs"))

    # Selecting LinkedIn link.
    page.locator(".social_linkedin > a:nth-child(1)").click()
    # expect(page).to_have_url(re.compile(".*linkedin.com"))