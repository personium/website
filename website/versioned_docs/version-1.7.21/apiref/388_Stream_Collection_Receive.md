---
id: version-1.7.21-388_Stream_Collection_Receive
title: Receive stream collection
sidebar_label: Receive stream collection
original_id: 388_Stream_Collection_Receive
---

## Overview
Receive data from stream collection queue

### Required Privileges
stream-receive

### Restrictions
* Accept in the request header is ignored
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body

## Request
### Request URL
```
{CellURL}{BoxName}/{CollectionName}/queue/{QueueName}
```

### Request Method
GET

### Request Query
None

### Request Header
|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### queue settings
It is necessary to register Queue name in [Configuration change](386_Configure_Stream_Collection.md) of Stream Collection.
If it is not registered, a 404 error will occur.

## Response
### Response Code
200

### Response Header
|Header Name|Overview|Notes|
|:--|:--|:--|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|
|Content-Type|Format of data to be returned||

### Response Body
JSON array

Because the message queue may retrieve multiple data, it returns an array response.
If there is no data sent, an empty array is returned.

### Error Messages
Refer to [Error Message List](004_Error_Messages.md)

## cURL Command
```sh
curl "https://cell1.unit1.example/box1/steram-colleciton1/queue/name" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA'
```
