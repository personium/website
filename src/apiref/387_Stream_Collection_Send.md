---
id: 387_Stream_Collection_Send
title: Send stream collection
sidebar_label: Send stream collection
---

## Overview
Send data to stream collection queue and topic

### Required Privileges
stream-send

## Request
### Request URL
```
{CellURL}{BoxName}/{CollectionName}/queue/{QueueName}
```
```
{CellURL}{BoxName}/{CollectionName}/topic/{TopicName}
```

### Request Method
POST<br>
PUT

### Request Query
None

### Request Header
|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/json|No|[application/json] by default|

### Request Body
JSON

There is no provision for Format.

### queue and topic
It is necessary to register Queue name and Topic name in [Change settings](386_Configure_Stream_Collection.md) of Stream Collection.
If it is not registered, a 404 error will occur.

The data sent to the queue can be obtained by [Receive](388_Stream_Collection_Receive.md) of Stream Collection.
However, since the queue can be acquired only once, it can not be acquired if someone receives it.

The data sent to topic can be obtained from [WebSocket connection](389_Stream_Collection_Connect.md) of Stream Collection.
However, you need to connect before sending. Only data sent after connection can be acquired.

## Response
### Response Code
200

### Response Header
|Header Name|Overview|Notes|
|:--|:--|:--|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body
None

### Error Messages
Refer to [Error Message List](004_Error_Messages.md)

## cURL Command
```sh
curl "https://cell1.unit1.example/box1/steram-colleciton1/queue/name" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-d '{"hoge":false,"piyo":"test"}'
```
