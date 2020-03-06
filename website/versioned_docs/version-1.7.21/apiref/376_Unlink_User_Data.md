---
id: version-1.7.21-376_Unlink_User_Data
title: Unlink Entity with other objects
sidebar_label: Unlink Entity with other objects
original_id: 376_Unlink_User_Data
---

## Overview

Delete $links information with Entity of user data


### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

#### $links with user data

```
{CellURL}{BoxName}/{CollectionName}/{EntityTypeName}('{EntityID}')/$links/_{EntityTypeName}('{EntityID}')
```

### Request Method

DELETE

### Request Query

#### Common Request Query

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only when no Authorization header is specified Specify when using authentication information of cookie|

#### OData Common Request Query

None

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

#### ODataDelete request header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|If-Match|Specifies the target ETag value|ETag value|No|[*] by default|

### Request Body

#### Format

JSON

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|uri|URI of the OData resource to be linked|Number of digits: 1-1024<br>Follow URI format<br>scheme:http / https / urn|Yes||

### Request Sample

None

## Response

### Response Code

204

### Response Header

#### Common Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

#### OData $links Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|DataServiceVersion|OData version||

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)



## cURL Command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1('{100-1_20101108-111352093}')\
/\$links/_entity-type1('{100-1_20101108-111352093}')" -X DELETE -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H \
'Accept: application/json'
```


