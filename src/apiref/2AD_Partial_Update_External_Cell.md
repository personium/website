---
id: 2AD_Partial_Update_External_Cell
title: Extcell partial update
sidebar_label: Extcell partial update
---

## Overview

Partial update of ExtCell

### Required Privileges

auth

### Restrictions

* Accept in the request header is ignored
* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* $formatQuery options ignored


## Request

### Request URL

```
{CellURL}__ctl/ExtCell('https%3A%2F%2F{CellName}.{UnitFQDN}%2F')
```

### Request Method

MERGE

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
|If-Match|Specifies the target ETag value|ETag value|No|[*] by default|

### Request Body

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Url|URL to Cell|Number of digits: 1-1024<br>Follow URI format<br>scheme:http, https<br>Trailing slash (URL terminated /) Required|No||

### Request Sample

```JSON
{
  "Url": "https://cell3.unit1.example/"
}
```


## Response

### Response Code

204

### Response Header

None

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/__ctl/ExtCell('https%3A%2F%2Fcell2.unit1.example%2F')" -X MERGE -i \
-H 'If-Match: *' -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '{"Url":"https://cell3.unit1.example/"}'
```

