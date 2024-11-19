# BUG REPORT-API:

### Subject:
Not possible to fail `/pet` POST request.

### Description:
The `/pet` endpoint allows the user to POST almost anything, and it will not throw a 405 error as expected.

### Steps to Reproduce:
**Via Swagger Doc**
1. Navigate to: `https://petstore.swagger.io/#/pet/addPet`
2. Select the `Try It Out` button
3. Add the following payload:
```
{
    "id": 77002,
    "category": {
        "id": 0,
        "name": 1
    },
    "name": 2,
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
        "id": 0,
        "name": 3
      }
    ],
    "status": "available"
}
```
4. Select `Execute`

### Notice:
The `POST` request will complete with a `200` code. The names are all integers instead of strings, which should return a `405` error by its own model listing.

### Expected:
The `POST` follows the stated model constraints as well as OpenAPI standards.