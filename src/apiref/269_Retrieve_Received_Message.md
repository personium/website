---
id: 269_Retrieve_Received_Message
title: Retrieve ReceivedMessage
sidebar_label: Retrieve ReceivedMessage
---

## Overview

acquire the List of ReceivedMessage

### Required Privileges

message or message-read

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

```
{CellURL}__ctl/ReceivedMessage('{MessageID}')
```

### Request Method

GET

### Request Query

The following query parameters are available

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

[$select  Query](406_Select_Query.md)

[$expand  Query](405_Expand_Query.md)

[$format  Query](404_Format_Query.md)

[$filter  Query](403_Filter_Query.md)

[$inlinecount  Query](407_Inlinecount_Query.md)

[$orderby  Query](400_Orderby_Query.md)

[$top  Query](401_Top_Query.md)

[$skip  Query](402_Skip_Query.md)

[Full-text Search (q) Query](408_Full_Text_Search_Query.md)

### Request Header

#### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|

#### OData Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

#### OData Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|
|If-None-Match|Specifies the target ETag value|ETag value|No|[*] by default|

### Request Body

None


## Response

### Response Code

200

### Response Header

None

### Response Body

#### Common

The response is a JSON object, the correspondence between the key (name) and type defined in the object (subobject) and the value are as follows

|Object|Name (Key)|Type|Value|
|:--|:--|:--|:--|
|Root|d|object|Object{1}|
|{1}|results|array|Array object {2}|
|{2}|__metadata|object|Object{3}|
|{3}|uri|string|URL to the resource that was created|
|{3}|etag|string|Etag value|
|{2}|__published|string|Creation date (UNIX time)|
|{2}|__updated|string|Update date (UNIX time)|
|{1}|__count|string|Get number of results in $inlinecount query|

#### ReceivedMessage specific response body

|Object|Name(Key)|Type|Value|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.ReceivedMessage|
|{2}|__id|string|ReceivedMessage ID<br>Return a 32 character string such as "b5d008e9092f489c8d3c574a768afc33" with UUID|
|{2}|_Box.Name|string|BoxName for Relation|
|{2}|InReplyTo|string|ID message you are replying<br>Return a 32 character string such as "b5d008e9092f489c8d3c574a768afc33" with UUID|
|{2}|From|string|From Cell URL|
|{2}|MulticastTo|string|Destination Cell URL<br>it becomes CSV format if it is sent to the plurality of Cell|
|{2}|Type|string|Message type<br>message : message<br>request : request|
|{2}|Title|string|Message Title|
|{2}|Body|string|Message Body|
|{2}|Priority|string|Priority<br>(high)1 - 5(low)|
|{2}|Status|string|Message Status<br>When Type is message<br> read: read<br> unread: unread<br>When type is request<br> approved: approved <br> rejected: rejected <br> none: none|
|{2}|RequestObjects|array|Request details<br>Array object {4}|
|{4}|RequestType|string|Request type|
|{4}|Name|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|ClassUrl|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|TargetUrl|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|EventType|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|EventSubject|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|EventObject|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|EventInfo|string|Refer to [SendMessage](271_Send_Message.md) for details|
|{4}|Action|string|Refer to [SendMessage](271_Send_Message.md) for details|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "{CellURL}__ctl/ReceivedMessage('c87b42e10df846a9bee842225d1383fe')",
        "etag": "W/\"1-1486683974451\"",
        "type": "CellCtl.ReceivedMessage"
      },
      "__id": "c87b42e10df846a9bee842225d1383fe",
      "_Box.Name": "{BoxName}",
      "InReplyTo": "xnKXmd4TTZCw-bfSEw4f0AxnKXmd4TTZ",
      "From": "{CellURL}",
      "MulticastTo": null,
      "Type": "request",
      "Title": "Message Sample Title",
      "Body": "It is the message text body.",
      "Priority": 3,
      "Status": "unread",
      "RequestObjects": [
        {
          "RequestType": "relation.add",
          "Name": null,
          "ClassUrl": "https://{UnitFQDN}/{AppCellName}/__relation/__/{RelationName}",
          "TargetUrl": "{CellURL}",
          "EventType": null,
          "EventSubject": null,
          "EventObject": null,
          "EventInfo": null,
          "Action": null
        }
      ],
      "__published": "/Date(1486683974451)/",
      "__updated": "/Date(1486683974451)/",
      "_Box": {
        "__deferred": {
          "uri": "{CellURL}__ctl/ReceivedMessage('c87b42e10df846a9bee842225d1383fe')/_Box"
        }
      },
      "_AccountRead": {
        "__deferred": {
          "uri": "{CellURL}__ctl/ReceivedMessage('c87b42e10df846a9bee842225d1383fe')/_AccountRead"
        }
      }
    }
  }
}
```


## cURL Command

```sh
curl "{CellURL}__ctl/ReceivedMessage('{MessageID}')" -X GET -i  -H \
'Authorization: Bearer {AccessToken}' -H 'Accept: application/json'
```
