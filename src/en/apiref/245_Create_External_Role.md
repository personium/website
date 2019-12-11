---
id: 245_Create_External_Role
title: Create ExtRole
sidebar_label: Create ExtRole
---

## Overview

register ExtRole

### Required Privileges

auth

### Restrictions

* OData Restrictions
    * Accept in the request header is ignored
    * Always handles Content-Type in the request header as application/json
    * Only accepts the request body in the JSON format
    * Only application/json is supported for Content-Type in the request header and the JSON format for the response body
    * $formatQuery options ignored


## Request

### Request URL

```
{CellURL}__ctl/ExtRole
```

### Request Method

POST

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/json|No|[application/json] by default|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|ExtRole|External Role Name(URL)|Number of digits: 1-1024<br>Follow URI format<br>scheme:http / https / urn<br>When associated with Box:/{Application CellName}/\_\_role/\_\_/{RoleName}<br>* However, if Schema information is not registered in Box, it is considered not to be associated with Box<br>When not associated with Box:{CellURL}\_\_role/\_\_/{RoleName}|Yes||
|_Relation.Name|Relation name of relationbr|Number of digits: 1 - 128<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("\_")<br> and +(plus) and :(colon)<br>However, the string cannot start with a underscore ("\_") or colon (:)<br>Relation which registered by Relation register API|Yes||
|_Relation._Box.Name|Box Name aassociated wirh Relation|Number of digits: 1 - 128<br>Character type: Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Box name associated with Relation registered by Relation registration API<br>null|No||

### Request Sample

```JSON
{
  "ExtRole": "https://cell2.unit1.example/__role/__/role1",
  "_Relation.Name": "relation1",
  "_Relation._Box.Name": "box1"  
}
```


## Response

### Response Code

201

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### OData Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|Location|URL to the resource that was created||
|DataServiceVersion|OData version||
|ETag|Resource version information||

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

### ExtRole specific response body

|Object|Item Name|Data Type|Notes|
|:--|:--|:--|:--|
|{3}|type|string|CellCtl.ExtRole|
|{2}|ExtRole|string|External Role URL|
|{2}|_Relation.Name|string|Relation Name|
|{2}|_Relation._Box.Name|string|Box Name aassociated wirh Relation|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/__ctl/ExtRole(ExtRole='https%3A%2F%2Fcell2.unit1.example
%2F__role%2F__%2Frole1',_Relation.Name='relation1',_Relation._Box.Name='box1')",
        "etag": "W/\"1-1486717404966\"",
        "type": "CellCtl.ExtRole"
      },
      "ExtRole": "https://cell2.unit1.example/__role/__/role1",
      "_Relation.Name": "relation1",
      "_Relation._Box.Name": "box1",
      "__published": "/Date(1486717404966)/",
      "__updated": "/Date(1486717404966)/"
    }
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/__ctl/ExtRole" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '{ "ExtRole": "https://cell2.unit1.example/__role/__/role1", "_Relation.Name": \
"relation1", "_Relation._Box.Name": "box1"}'
```
