import re
import creds
from playwright.sync_api import Page, expect, sync_playwright

def test_filtering(page: Page):
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

# Filtering:

    # Ascending.
    page.locator(".product_sort_container").click()
    page.locator(".product_sort_container").select_option(value="az")
    expect(page.locator("#item_4_title_link > div:nth-child(1)")).to_have_text("Sauce Labs Backpack")

    # Descending.
    page.locator(".product_sort_container").click()
    page.locator(".product_sort_container").select_option(value="za")
    expect(page.locator("#item_3_title_link > div:nth-child(1)")).to_have_text("Test.allTheThings() T-Shirt (Red)")

    # Price ascending.
    page.locator(".product_sort_container").click()
    page.locator(".product_sort_container").select_option(value="lohi")
    expect(page.locator("#item_2_title_link > div:nth-child(1)")).to_have_text("Sauce Labs Onesie")

    # Price descending.
    page.locator(".product_sort_container").click()
    page.locator(".product_sort_container").select_option(value="hilo")
    expect(page.locator("#item_5_title_link > div:nth-child(1)")).to_have_text("Sauce Labs Fleece Jacket")    