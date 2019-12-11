---
id: 258_Retrieve_Box
title: Retrieve Box
sidebar_label: Retrieve Box
---

## Overview

Obtain existing Box information

### Required Privileges

box-read

### Restrictions

* Accept in the request header is ignored
* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* $formatQuery options ignored


## Request

### Request URL

```
{CellURL}__ctl/Box('{BoxName}')
```

or 

```
{CellURL}__ctl/Box(Name='{BoxName}')
```

### Request Method

GET

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

[$select  Query](406_Select_Query.md)

[$expand  Query](405_Expand_Query.md)

[$format  Query](404_Format_Query.md)

### Request Header

### Request Body

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|
|If-None-Match|Specifies the target ETag value|ETag value|No|[*] by default|


## Response

### Response Code

200

### Response Header

None

### Response Body

The response is a JSON object, the correspondence between the key (name) and type defined in the object (subobject) and the value are as follows

|Object|Item Name|Data Type|Notes|
|:--|:--|:--|:--|
|Root|d|object|Object{1}|
|{1}|results|array|Array object {2}|
|{2}|__metadata|object|Object{3}|
|{3}|uri|string|URL to the resource that was created|
|{3}|etag|string|Etag value|
|{2}|__published|string|Creation date (UNIX time)|
|{2}|__updated|string|Update date (UNIX time)|
|{1}|__count|string|Get number of results in $inlinecount query|

### Box specific response body

|Object|Item Name|Data Type|Notes|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.Box|
|{2}|Name|string|Box Name|
|{2}|Schema|string|Schema Name|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/__ctl/Box('box1')",
        "etag": "W/\"1-1486368212581\"",
        "type": "CellCtl.Box"
      },
      "Name": "box1",
      "Schema": null,
      "__published": "/Date(1486368212581)/",
      "__updated": "/Date(1486368212581)/",
      "_Role": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/__ctl/Box('box1')/_Role"
        }
      },
      "_Relation": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/__ctl/Box('box1')/_Relation"
        }
      },
      "_ReceivedMessage": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/__ctl/Box('box1')/_ReceivedMessage"
        }
      },
      "_SentMessage": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/__ctl/Box('box1')/_SentMessage"
        }
      },
      "_Rule": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/__ctl/Box('box1')/_Rule"
        }
      }
    }
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/__ctl/Box('box1')" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```


