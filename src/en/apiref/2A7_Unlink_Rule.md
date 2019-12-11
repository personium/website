---
id: 2A7_Unlink_Rule
title: Unlink Rule with other objects
sidebar_label: Unlink Rule with other objects
---
## Overview

Release the link with Box linked from Rule.

### Required Permissions
* rule
* box

### Limitations

* Content-Type of the response header supports only application / json, and the response body is JSON format

## request
### Request URL
```
{CellURL}__ctl/Rule(Name='{RuleName}',_Box.Name='{BoxName}')/$links/_Box(Name='{BoxName}')
```
Alternatively,
```
{CellURL}__ctl/Rule(Name='{RuleName}',_Box.Name='{BoxName}')/$links/_Box('{BoxName}')
```

### Method
DELETE
### Request query

| Query name | Summary | Valid values ​​| Required | Remarks |
|:--|:--|:--|:--|:--|
| p_cookie_peer | cookie authentication value | cookie authentication value returned from the server at the time of authentication | No | valid only when there is no specification of the authorization header <br> specifying when using the authentication information of the cookie |

### Request Header

| Header name | overview | effective value | required | remarks |
|:--|:--|:--|:--|:--|
| X-HTTP-Method-Override | method override function | optional | No | If you specify this value when requesting with the POST method, the specified value will be used as a method. |
| X-Override|header override function|${overwrite header name}:${value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
| X-Personium-RequestKey |RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
| Authorization | Specify authentication information in OAuth 2.0 format | Bearer {AccessToken} | No | * Authentication token acquired with the authentication token acquisition API Token |
| If-Match | Specify target ETag value | ETag value | No | treat as [*] when omitted |
### Request body
None

## Response
### Status code
204
### Response header

| Header name | Overview | Remarks |
|:--|:--|:--|
| DataServiceVersion | OData version ||
| Access-Control-Allow-Origin | Cross-domain communication permission header | Return value is fixed as "*"
| X-Personium-Version | Execution version of API | API version processed request |

### Response body
None

### Error message list
[Error message list](004_Error_Messages.md) is referred to

## cURL Sample

```sh
curl "https://cell1.unit1.example/__ctl/Rule(Name='rule1',\
_Box.Name='box1')/\$links/_Box(Name='box2')" \
-X DELETE -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```
