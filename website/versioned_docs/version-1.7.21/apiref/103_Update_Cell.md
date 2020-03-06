---
id: version-1.7.21-103_Update_Cell
title: Update Cell
sidebar_label: Update Cell
original_id: 103_Update_Cell
---

## Overview

Updating existing cell information

### Required Privileges

Only unit users permitted

### Restrictions

* OData Restrictions
    * Always handles Content-Type in the request header as application/json
    * Only accepts the request body in the JSON format
    * Only application/json is supported for Content-Type in the request header and the JSON format for the response body
    * Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

```
{UnitURL}__ctl/Cell(Name='{CellName}')
```

or

```
{UnitURL}__ctl/Cell('{CellName}')
```

### Request Method

PUT

### Request Query

None

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/json|No|[application/json] by default|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|
|If-Match|Specifies the target ETag value|ETag value|No|[*] by default|

### Request Body

#### Format

JSON

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Name|Cell name|Number of digits: 1 - 128<br>Character type: Single-byte alphanumeric characters(lower case), hyphens("-")<br>However, the string cannot start with a hyphens("-")|Yes||

### Request Sample

```JSON
{"Name":"cell2"}
```


## Response

### Response Code

204

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|ETag|Resource version information||
|DataServiceVersion|OData version||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|Personium API version|Version of the API used to process the request|

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://unit1.example/__ctl/Cell(Name='cell1')" -X PUT -i -H \
'Authorization: Bearer PEFzc2V...(snip)...lvbj4' -H 'Accept: application/json' -d '{"Name":"cell2"}'
```

