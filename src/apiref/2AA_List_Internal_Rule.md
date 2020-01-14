---
id: 2AA_List_Internal_Rule
title: Retrieve List of Internal Rule information
sidebar_label: Retrieve List of Internal Rule information
---

## Overview
Retrieve list of internal rule information

### Required Permissions
rule-read

## request
### Request URL
```
{CellURL}__rule
```
### Method
GET

### Request Query
The following query parameters are available.

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header
|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|


### Request Body
None

## Response
### Response Code
200

### Response Header
|Header Name|Overview|Notes|
|:--|:--|:--|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### OData Response Header
|Header name|Overview|Remarks|
|:--|:--|:--|
|Content-Type|Format of data to be returned||

### Response Body
The response is a JSON object.

### Error Messages
Refer to [Error Message List](004_Error_Messages.md)

## cURL Command

```sh
curl "https://cell1.unit1.example/__rule" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```
