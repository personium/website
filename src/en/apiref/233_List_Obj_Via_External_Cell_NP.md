---
id: 233_List_Obj_Via_External_Cell_NP
title: Retrieve other objects list via ExtCell's Navigation Property
sidebar_label: Retrieve other objects list via ExtCell's Navigation Property
---

## Overview

Retrieve cell control object via Navigation Property

### Required Privileges

* Reference authority for both the cell control object to be acquired and the cell control object via which it is acquired
* Example) When acquiring Relation via Role<br>Auth-read and social-read

### Restrictions

* Accept in the request header is ignored
* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* $formatQuery options ignored


## Request

### Request URL

#### Navigation Property to Role

```
{CellURL}__ctl/ExtCell(Url='https%3A%2F%2F{CellName}.{UnitFQDN}%2F')/_Role
```

or 

```
{CellURL}__ctl/ExtCell('https%3A%2F%2F{CellName}.{UnitFQDN}%2F')/_Role
```

#### Navigation Property to Relation

```
{CellURL}__ctl/ExtCell(Url='https%3A%2F%2F{CellName}.{UnitFQDN}%2F')/_Relation
```

or 

```
{CellURL}__ctl/ExtCell('https%3A%2F%2F{CellName}.{UnitFQDN}%2F')/_Relation
```

\* URL encoding required for {ExtCellURL}

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

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
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
|Content-Type|Format of data to be returned||
|DataServiceVersion|OData version||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

|Object|Item Name|Data Type|Remarks|
|:--|:--|:--|:--|
|Root|d|object|Object{1}|
|{1}|results|array|Array object {2}|
|{2}|__metadata|object|Object{3}|
|{3}|uri|string|URL to the resource that was created|
|{3}|etag|string|Etag value|
|{2}|__published|string|Creation date (UNIX time)|
|{2}|__updated|string|Update date (UNIX time)|
|{1}|__count|string|Get number of results in $inlinecount query|

#### When acquired ExtCell

#### ExtCell specific response body

|Object|Item Name|Data Type|Remarks|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.ExtRole|
|{2}|Name|string|Role name to be related|
|{2}|_Box.Name|string|Box name to be related|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample
```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1',_Box.Name='box1')",
          "etag": "W/\"1-1487320623218\"",
          "type": "CellCtl.Role"
        },
        "Name": "role1",
        "_Box.Name": "box1",
        "__published": "/Date(1487320623218)/",
        "__updated": "/Date(1487320623218)/",
        "_Box": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1'
,_Box.Name='box1')/_Box"
          }
        },
        "_Account": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1'
,_Box.Name='box1')/_Account"
          }
        },
        "_ExtCell": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1'
,_Box.Name='box1')/_ExtCell"
          }
        },
        "_ExtRole": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1'
,_Box.Name='box1')/_ExtRole"
          }
        },
        "_Relation": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1'
,_Box.Name='box1')/_Relation"
          }
        }
      }
    ]
  }
}
```

## cURL Command

### Through Role's Navigation Property list

```sh
curl "https://cell1.unit1.example/__ctl/ExtCell('https%3A%2F%2Fcell2.unit1.example%2F')/_Role" \
-X GET -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

