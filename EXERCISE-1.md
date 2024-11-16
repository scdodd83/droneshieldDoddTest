# TEST-STRATEGY

## OBJECTIVES

The purpose of this doc is to outline and define the test strategy for the `saucedemo` store front. 

## SCOPE

The tests will cover all pages within the `saucedemo` domain, including, but not limited to:

* Login page
* Home/Store Page
* Navigation options
* Item details pages
* Cart usage
* Error handling

## METHODOLOGY

We will be using Playwright and PyTest to complete the tests. The tests are to be written in python at the client's request, and a report will be provided after each testing run.

# TEST-PLANS

`Saucedemo` URL: https://www.saucedemo.com/

## LOGIN PAGE TESTS

* `Standard_user` is able to log in
* `Standard_user` is able to log out
* `Locked_out` user is unable to login
* `Locked_out` user is shown an error message
* User is unable to login with incorrect credentials

## HOME/STORE PAGE TESTS

* User is shown the store page on login
* User can expand/collapse the flyout navigation
* User can select the `X` (formerly Twitter) link
* User can select the `Facebook` link
* User can select the `LinkedIn` link
* User is able to filter alphabetically in ascending order
* User is able to filter alphabetically in descending order
* User is able to filter by price in ascending order
* User is able to filter by price in descending order

## ITEM DETAILS AND CART TESTS

* User is able to select an item name link from the store page
* Selecting an item in the store page takes the user to the item details page
* User can select `Add to cart` from the item details page
* Adding an item from the item details page adds the item to the cart
* User can select `Remove` from the item details page
* Selecting `Remove` from the item details page reoves the item from the cart
* Selecting `Back to products` link takes the user pack to the store page
* Selecting `Add to cart` adds the selected item to the cart
* `Remove` button appears for items currently in the cart
* Selecting `Remove` removes the item from the cart
* Number of items in cart is displayed correctly on button
* Selecting the cart button takes the user to the cart page
* `Continue Shopping` button takes the user back to the previous page
* Selecting `Remove` from cart page removes the item from the cart
* Selecting item link in cart takes user to the item page

## CHECKOUT TESTS

* Selecting `Checkout` takes user to the checkout page
* User is able to fill in personal information fields
* User is unable to continue without all necessary fields filled in
* Selecting `Cancel` takes the user back to the cart
* Selecting `Continue` takes the user to the Overview page
* Selecting `Cancel` on Overview page takes user back to store page
* Selecting `Finish` shows user the order completion page
* Selecting `Back Home` takes user to the store page

# DECISIONS AND REASONS

Here's my reasoning.