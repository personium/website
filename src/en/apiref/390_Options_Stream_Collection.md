---
id: 390_Options_Stream_Collection
title: Get operational method of Stream collection
sidebar_label: Get operational method of Stream collection
---

## Overview
Return the methods that can be operated on Stream collection according to the token's authority.

### Required Privileges
None

## Request
### Request URL
```
{CellURL}{BoxName}/{CollectionName}/queue/{QueueName}
```
```
{CellURL}{BoxName}/{CollectionName}/topic/{TopicName}
```

### Request Method
OPTIONS

### Request Query
|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header
|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

\* Authentication information is required. If there is no authentication information, the response of the OPTIONS method will be that with all methods set in the Allow header.

## Response
### Response Code
200

### Response Header
|Header Name|Overview|Notes|
|:--|:--|:--|
|Access-Control-Allow-Methods|CORS header|Refer to [CORS Support](002_CORS_Support.md)|
|Allow|Manipulatable method|OPTIONS and POST and PUT if send is possible. OPTIONS and GET if receive is possible. OPTIONS and POST and PUT and GET if both are possible. OPTIONS if both are not possible.|

### Response Body
None

### Error Messages
Refer to [Error Message List](004_Error_Messages.md)

## cURL Command
```sh
curl "https://cell1.unit1.example/box1/stream-collection1/queue/name" -X OPTIONS -i -H \
"Authorization:Bearer AA~PBDc...(snip)...FrTjA"
```
