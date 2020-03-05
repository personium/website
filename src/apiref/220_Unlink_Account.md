---
id: 220_Unlink_Account
title: Unlink Account with other objects
sidebar_label: Unlink Account with other objects
---

## Overview

Delete a list of OData resources associated with Account

### Restrictions

* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* Response body data is not ensured if atom or xml is specified in the $format query option, although it does not result in an error


## Request

### Request URL

link with Role

```
{CellURL}__ctl/Account(Name='{AccountName}')/$links/_Role(Name='{RoleName}',_Box.Name='{BoxName}')
```

or

```
{CellURL}__ctl/Account(Name='{AccountName}')/$links/_Role(Name='{RoleName}')
```

or

```
{CellURL}__ctl/Account(Name='{AccountName}')/$links/_Role('{RoleName}')
```

or

```
{CellURL}__ctl/Account('{AccountName}')/$links/_Role(Name='{RoleName}',_Box.Name='{BoxName}')
```

or

```
{CellURL}__ctl/Account('{AccountName}')/$links/_Role(Name='{RoleName}')
```

or

```
{CellURL}__ctl/Account('{AccountName}')/$links/_Role('{RoleName}')
```

### Request Method

DELETE

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
|If-Match|Specifies the target ETag value|ETag value|No||

### Request Body

None


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
curl "https://cell1.unit1.example/__ctl/Account('account1')/\$links/_Role('role1')" -X DELETE -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```


