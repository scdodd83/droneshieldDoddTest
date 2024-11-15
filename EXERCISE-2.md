# TEST-STRATEGY

## OBJECTIVES

The purpose of this doc is to outline and define the test strategy for the `petstore` API. 

## SCOPE

The tests will cover all API calls available in the Swagger doc. The call types available are:

* POST
* PUT
* GET
* DELETE

The calls are grouped by the following description:

* Pet - these calls deal with the individual pets adn their information
* Store - these calls deal with the store and its function
* User - these calls handle all user functionality

## METHODOLOGY

# TEST-PLANS

SWAGGER DOC: https://petstore.swagger.io/

## PET TESTS

* Add pet to the store
* Add image for the pet
* Update created pet entry status
* Fetch pet entry by updated status
* Find created pet
* Search for non-existent pet
* Update pet name in DB
* Delete created pet entry
* Check error with incorrect entry

## PET STORE TESTS

* Get store inventory
* Place an order
* Get the created order by ID
* Delete the created order
* Check error with incorrect entry

## STORE USER TESTS

* Create array of users with list
* Create array of users with array
* Create a new user
* Get the created user
* Log new user in
* Log new user out
* Edit user's name
* Delete the created user
* Check error with incorrect entry

# DECISIONS AND REASONS

Here's my reasoning.