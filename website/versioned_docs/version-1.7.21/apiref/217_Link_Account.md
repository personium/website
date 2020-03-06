---
id: version-1.7.21-217_Link_Account
title: Link other objects with Account
sidebar_label: Link other objects with Account
original_id: 217_Link_Account
---

## Overview

Link Account to the OData resource specified by $links  
Get a list of OData resources linked with following

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

When linking with Role

```
{CellURL}__ctl/Account(Name='{AccountName}')/$links/_Role
```

or

```
{CellURL}__ctl/Account('{AccountName}')/$links/_Role
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
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/json|No|[application/json] by default|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

JSON

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|uri|URI of the OData resource to be linked|Number of digits: 1-1024<br>Follow URI format<br>scheme:http / https / urn|Yes||

### Request Sample

```JSON
{"uri":"https://cell1.unit1.example/__ctl/Box('box1')"}
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
curl "https://cell1.unit1.example/__ctl/Account(Name='account1')/\$links/_Role" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d "{\"uri\":\"https://cell1.unit1.example/__ctl/Role(Name='role1',_Box.Name='box1')\"}"
```

