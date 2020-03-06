---
id: version-1.7.21-297_OAtuh2_Token_Introspection_Endpoint
title: OAuth 2.0 Token Introspection Endpoint
sidebar_label: OAuth 2.0 Token Introspection Endpoint
original_id: 297_OAtuh2_Token_Introspection_Endpoint
---
## Overview
It is the API endpoint that acquires the contents of the token. Implements RFC 7662.

It returns results only if the token Issuer or Audience is equal to CellURL.

### Required Privileges
None

### Restrictions
* Accept in the request header is ignored
* We treat all Content-Type of the request header as application/x-www-form-urlencoded
* The response header Content-Type supports only application/json, and the response body is JSON format

## Request
### Request URL
```
{CellURL}/__introspect
```
### Request Method
POST

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specify authentication information in OAuth 2.0 format|Bearer {Token}<br>Basic {Base64String}|○|In the case of Bearer, the authentication token is the access token acquired by the authentication token acquisition API. It is possible to acquire token information only when unit token or unit user token or Schema of token matches Schema of token specified by request body.<br>For Basic, user name and password are those set for Introspection by Unit setting, or CellURL and token are specified. In the case of CellURL and token, token information can be obtained only when client authentication is OK and CellURL is token that matches Schema|
|Content-Type|Specify the format of the request body|application/x-www-form-urlencoded|×|When omitted, treat it as [application/x-www-form-urlencoded]|
|Accept|Specify the format of the response body|application/json|×|When omitted, treat it as [application/json]|

### Request Body

|Item Name|Overview|Format|Required|Effective Value|
|:--|:--|:--|:--|:--|
|token|Token|String|○|Access Token or Refresh Token Acquired with Authentication Token Acquisition API|

### Request Sample

```
token=AA~(snip)

```

## Response
### Response Code
200

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|application/json||

### レスポンスボディ

|Item Name|Overview|Type|Notes|
|:--|:--|:--|:--|
|active|Whether the token is valid|boolean||
|client_id|ClientID|string|In personium the schema of the token|
|exp|expiration date|integer|January 1 1970 Number of seconds since UTC|
|iat|Issue time|integer|January 1 1970 Number of seconds since UTC|
|sub|Main token|string|In personium the subject of the token|
|aud|Token Audience|string|In personium the target in the transcell token|
|iss|Issuer of the token|string|The URL of the cell that issued the token|
|p_roles|List of roles contained in the token|list of string|personium proprietary specification|

### Response Sample
For valid tokens
```JSON
{
  "active": true,
  "exp": 1544059820,
  "iat": 1543973420,
  "sub": "https://cell1.unit1.example/#account",
  "aud": "https://cell2.unit1.example/",
  "iss": "https://cell1.unit1.example/",
  "p_roles": ["https://cell1.unit1.example/__role/__/role1","https://cell1.unit1.example/__role/__/role2"]
}
```
For invalid token
```JSON
{
  "active": false,
}
```

### Error Messages
Refer to [Error Message List](004_Error_Messages.md)

## cURL Command
```sh
curl "https://cell1.unit1.example/__introspect" -X POST -i \
-H 'Authorization:Basic username:password' \
-H 'Content-Type:application/x-www-form-urlencoded' \
-H 'Accept:application/json' \
-d 'token=RA~(snip)'
```
