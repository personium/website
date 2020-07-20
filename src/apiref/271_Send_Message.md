---
id: 271_Send_Message
title: Send Message
sidebar_label: Send Message
---

## Overview

send message

### Required Privileges

message

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

```
{CellURL}__message/send
```

### Request Method

POST

### Request Query

None

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/json|No|[application/json] by default|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

JSON

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|BoxBound|Linking with Box, whether possible or not|true / false<br>The default value is false|No|Send a token you have schema authentication is set to true this item when you tie in Box (not implemented)|
|InReplyTo|Message ID of the reply message|Number of digits: 32<br>null|No||
|To|Destination cell URL|URL format<br>null|* 1|If you want to send message to multiple cells specified in CSV format,<br>*1 required either Relation or To<br>Maximum 1000 cell URL destination can be specified in Relation or To|
|ToRelation|Relationship names to be sent|Number of digits: 1 - 128<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("\_"), plus, :<br>However, the string cannot start with a underscore ("\_") or colon (:)<br>null|* 1|*1 required either Relation or To<br>Maximum 1000 cell URL destination can be specified in Relation or To|
|Type|Message type|message<br>req.relation.build<br>req.relation.break<br>req.role.grant<br>req.role.revoke|No|The message is treated as a default|
|Title|Message Title|Number of digits: 256 characters or less|No|The default is treated as an empty string|
|Body|Message Body|Number of digits: 64Kbyte following|No|The default is treated as an empty string|
|Priority|Priority|1~5|No|The default is treated as 3|
|RequestRelation|Information of requested relation to register|URL format<br>null|* 2|*2 Required when message type is other than message<br>Relation name or relation class URL or role name or role class URL, the registration request<br>When only the relation name is specified, it is regarded as a relative URL from the following URL<br>BoxBound is true:[target Box schema URL]\_\_relation/\_\_/<br>BoxBound is false:[destination cell URL]\_\_relation/\_\_/<br>When only the role name is specified, it is regarded as a relative URL from the following URL<br>BoxBound is true:[target Box schema URL]\_\_role/\_\_/<br>BoxBound is false:[destination cell URL]\_\_role/\_\_/|
|RequestRelationTarget|Cell URL that connects the relationship|URL format<br>null|* 2|*2 Required when message type is other than message|
|RequestObjects|Request details|JSON array|* 2|*2 Required when Type is request<br>For details, refer to RequestObject below|

#### RequestObject
Describe details of the request.  
The content varies depending on the Type specified in RequestType.  

##### Relation add/remove
RequestType : relation.add / relation.remove  
Ask Relation specified by Name or ClassUrl and link / unlink of Cell specified by TargetUrl.  

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|RequestType|Request type|relation.add<br>relation.remove|Yes||
|Name|Relation name|Number of digits: 1 - 128<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("\_"), plus, :<br>However, the string cannot start with a underscore ("\_") or colon (:)|*1|*1 Either Name or ClassUrl is required<br>When Name is specified, it is regarded as a relative URL from the following URL<br>BoxBound is true:[target Box schema URL]\_\_relation/\_\_/<br>BoxBound is false:[destination cell URL]\_\_relation/\_\_/|
|ClassUrl|Relation class URL|Relation class URL<br>See the [glossary](../introduction/008_Glossary.md#anc_r) for details|*1|*1 Either Name or ClassUrl is required|
|TargetUrl|Cell URL that connects the relationship|URL format|Yes||

##### Role add/remove
RequestType : role.add / role.remove  
Ask Role specified by Name or ClassUrl and link / unlink of Cell specified by TargetUrl.  

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|RequestType|Request type|role.add<br>role.remove|Yes||
|Name|Role name|Number of digits: 1 - 128<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("\_")<br>However, the string cannot start with a single-byte hyphen ("-") or underscore ("\_")|*1|*1 Either Name or ClassUrl is required<br>When Name is specified, it is regarded as a relative URL from the following URL<br>BoxBound is true:[target Box schema URL]\_\_role/\_\_/<br>BoxBound is false:[destination cell URL]\_\_role/\_\_/|
|ClassUrl|Role class URL|Role class URL<br>See the [glossary](../introduction/008_Glossary.md#anc_r) for details|*1|*1 Either Name or ClassUrl is required|
|TargetUrl|Cell URL that connects the relationship|URL format|Yes||

##### Rule add/remove
RequestType : rule.add / rule.remove  
Ask the creation / deletion of the specified Rule.  

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|RequestType|Request type|rule.add<br>rule.remove|Yes||
|Name|Arbitrary name to make the rule to be created identifiable|See the [CreateRule](2A0_Create_Rule.md) for details|No||
|EventType|Type of the event to trigger the rule|See the [CreateRule](2A0_Create_Rule.md) for details|No||
|EventSubject|Event Subject to trigger the rule|See the [CreateRule](2A0_Create_Rule.md) for details|No|On message, not check if this item is able to convert to personium-localunit scheme.|
|EventObject|Event Object prefix to trigger the rule|See the [CreateRule](2A0_Create_Rule.md) for details|No||
|EventInfo|Event Info prefix to trigger the rule|See the [CreateRule](2A0_Create_Rule.md) for details|No||
|Action|Action to invoke when the matching event is met|See the [CreateRule](2A0_Create_Rule.md) for details|Yes||
|TargetUrl|Specific target url of the action|See the [CreateRule](2A0_Create_Rule.md) for details|No|On message, not check if this item is able to convert to personium-localunit scheme.|

### Request Sample
```JSON
{
  "BoxBound": true,
  "InReplyTo": "hnKXm44TTZCw-bfSEw4f0A",
  "To": "https://cell2.unit1.example/",
  "ToRelation": null,
  "Type": "request",
  "Title": "Friend request",
  "Body": "Thank you for the friend approval",
  "Priority": 3,
  "RequestObjects": [
    {
      "RequestType": "relation.add",
      "ClassUrl": "https://app-cell1.unit1.example/__relation/__/relation1",
      "TargetUrl": "https://cell2.unit1.example/"
    },
    {
      "RequestType": "role.add",
      "Name": "role1",
      "TargetUrl": "https://cell2.unit1.example/"
    }
  ]
}
```


## Response

### Response Code

201

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|Location|URL to the resource that was created||
|DataServiceVersion|OData version||
|ETag|Resource version information||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

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

#### SentMessage specific response body

|Object|Name (Key)|Type|Value|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.ReceivedMessage|
|{2}|__id|string|ReceivedMessage ID<br>Return a 32 character string such as "b5d008e9092f489c8d3c574a768afc33" with UUID|
|{2}|InReplyTo|string|ID message you are replying<br>Return a 32 character string such as "b5d008e9092f489c8d3c574a768afc33" with UUID|
|{2}|To|string|Destination cell URL|
|{2}|ToRelation|string|Relationship names to be sent|
|{2}|Type|string|Message type<br>message: message<br>request: request|
|{2}|Title|string|Message Title|
|{2}|Body|string|Message Body|
|{2}|Priority|string|Priority<br>(high)1 - 5(low)|
|{2}|RequestObjects|array|Request details<br>Array object {4}|
|{4}|RequestType|string|Request type|
|{4}|Name|string|Refer to Request Body for details|
|{4}|ClassUrl|string|Refer to Request Body for details|
|{4}|TargetUrl|string|Refer to Request Body for details|
|{4}|EventType|string|Refer to Request Body for details|
|{4}|EventSubject|string|Refer to Request Body for details|
|{4}|EventObject|string|Refer to Request Body for details|
|{4}|EventInfo|string|Refer to Request Body for details|
|{4}|Action|string|Refer to Request Body for details|
|{2}|_Box.Name|string|BoxName for Relation|
|{2}|Result|array|Transmission result of each destination Cell<br>Array object {5}|
|{5}|To|string|Destination cell URL|
|{5}|Code|string|Response Code|
|{5}|Reason|string|Detailed message|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/__ctl/SentMessage
('3afcc60e35fc49ee9a4e4f6c1ebee426')",
        "etag": "W/\"1-1486638759524\"",
        "type": "CellCtl.SentMessage"
      },
      "__id": "3afcc60e35fc49ee9a4e4f6c1ebee426",
      "InReplyTo": "xnKXmd4TTZCw-bfSEw4f0AxnKXmd4TTZ",
      "To": "https://cell2.unit1.example/",
      "ToRelation": null,
      "Type": "request",
      "Title": "Message Sample Title",
      "Body": "Message Sample Body",
      "Priority": 3,
      "RequestObjects": [
        {
          "RequestType": "relation.add",
          "Name": null,
          "ClassUrl": "https://app-cell1.unit1.example/__relation/__/relation1",
          "TargetUrl": "https://cell2.unit1.example/",
          "EventType": null,
          "EventSubject": null,
          "EventObject": null,
          "EventInfo": null,
          "Action": null
        }
      ],
      "_Box.Name": null,
      "Result": [
        {
          "To": "https://cell2.unit1.example/",
          "Code": "201",
          "Reason": "Created."
        }
      ],
      "__published": "/Date(1486638759524)/",
      "__updated": "/Date(1486638759524)/"
    }
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/__message/send" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '{"BoxBound":false,"InReplyTo":"xnKXmd4TTZCw-bfSEw4f0AxnKXmd4TTZ",\
"To":"https://cell2.unit1.example/","Type":"message","Title":"Message Sample Title","Body":"Message Sample Body",\
"Priority":3}'
```
