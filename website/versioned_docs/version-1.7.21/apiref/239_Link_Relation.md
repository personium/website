---
id: version-1.7.21-239_Link_Relation
title: Link other objects with Relation
sidebar_label: Link other objects with Relation
original_id: 239_Link_Relation
---

## Overview

Link Relation to the OData resource specified by $links  
Get a list of OData resources linked with following  

* Box
* ExtCell
* ExtRole
* Role

Only when the \_Box.Name described in the request URL is null (or if it is not specified) can be associated with Box

### Restrictions

* Accept in the request header is ignored
* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* $formatQuery options ignored


## Request

### Request URL

#### Correlating with Box

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_Box
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_Box
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_Box
```

#### Correlating with ExtCell

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_ExtCell
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtCell
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtCell
```

#### Correlating with ExtRole

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_ExtRole
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtRole
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtRole
```

#### Correlating with the role

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_Role
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_Role
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_Role
```

If the \_Box.Name parameter is omitted, it is assumed that null is specified

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
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/json|No|[application/json] by default|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

#### Format

JSON

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|uri|URI of the OData resource to be linked|Number of digits: 1-1024<br>Follow URI format<br>scheme:http / https / urn|Yes||

### Request Sample

```JSON
{"uri":"https://cell1.unit1.example__ctl/Role(Name='role1',_Box.Name='box1')"}
```


## Response

### Response Code

204

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|DataServiceVersion|OData version||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/__ctl/Relation(Name='relation1',_Box.Name='box1')\
/\$links/_Role" -X POST -i  -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json' \
-d "{\"uri\":\"https://cell1.unit1.example/__ctl/Role(Name='role1',_Box.Name='box1')\"}"
```


