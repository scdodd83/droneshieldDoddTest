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

I have written a out a full API automation suite for the `petstore` swagger doc. I went through and wrote individual scripts for each API call in the doc. I thought about creating one large API test so as to cut down on time and redundancy, but I ultimately opted for separate tests to allow more granular viewing and a little cleaner reference for anyone viewing these scripts. It was interesting. I'm not sure who wrote the swagger doc, but it does not adhere to OpenAPI standards. I chose to assume that it was on purpose. Things like the verbiage did not adhere to plurality, there isn't a call to get a list of all users, there's a POST call that also requires an ID, which goes against the general idea of a POST creating something. If you're creating it, it won't have an ID yet. The user's ability to create their own IDs as opposed to assigning an ID upon content creation. There was a lot. I assumed those choices were on purpose to see if they were noticed.

That being said, I went and used the same framework of `Pytest` and `Playwright` for the API tests so everything could be ran in one go. I thought about adding test hooks to separate, but ran out of time. Figured this was sufficient to show the general flow and structure. There are scripted failures in the API tests, so when they fail, you'll note why. One of them I used as the bug report in [BUGREPORT-2.md](BUGREPORT-1.md). It was impossible to fail, which went against its own model. Feel free to contact me with any questions. My contact information is in the [README.md](README.md). Thank you.