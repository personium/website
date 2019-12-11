---
id: 304_Get_Box_URL
title: Retrieve BoxURL
sidebar_label: Retrieve BoxURL
---

## Overview

It is a resource used to obtain the URL of Box. The application that performed the schema authentication redirects to the Box URL for the schema - authenticated application by accessing this resource with an access token.  
An application that does not support schema authentication redirects to the URL of the corresponding Box by giving schema url as a parameter.

### Required Privileges

It is necessary to satisfy either of the followings.

* Schema authenticated
* If the requireSchemaAuthz attribute of the Box root ACL is none  
and  
The user can read the Box route. (User authentication is unnecessary when the Box route is open to the public)

\*For the requireSchemaAuthz attribute of the ACL, see "Schema Privilege Request Level" in the [access control model](006_Access_Control.md).


## Request

### Request URL

```
{CellURL}__box
```

### Request Method

GET

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|
|schema|App cell URL|URL format|No|Number of digits: 1-1024<br>Follow URI format|

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value} override} $: $ {value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

### Request Body

None


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|200|FOUND|Acquisition success|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Location|URL for Box metadata acquisition API|Depending on the request specification method, the following values are obtained<br>Specify schema query<br>chema Box URL corresponding to the app cell URL specified in the query<br>Specify only Authorization header without schema query<br>Box URL corresponding to the schema URL included in the token|

Location sample

```
Location:https://cell1.unit1.example/box1
```

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```
Location:https://cell1.unit1.example/box1
```


## cURL Command

### Schema authenticated

```sh
curl "https://cell1.unit1.example/__box" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

### Schema authentication not supported

```sh
curl "https://cell1.unit1.example/__box?schema=https://app-cell1.unit1.example/" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

