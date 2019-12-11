---
id: 2A5_Link_Rule
title: Link other objects with Rule
sidebar_label: Link other objects with Rule
---
## Overview
You can link Rule to OData resource below  
linking OData resource specified by $ links
* Box

Only when the _Box.Name described in the request URL is null (or if it is not specified) can be associated with Box

### Required Permissions

* rule
* box

### Limitations
* Accept of request header is ignored
* Treat all Content-Type of the request header as application / json
* Accept only JSON format for request body
* Content-Type of the response header supports only application / json, and the response body is JSON format
* $ format query option ignored

## request
### Request URL
```
{CellURL}__ctl/Rule(Name='{RuleName}')/$links/_Box
```
Alternatively,
```
{CellURL}__ctl/Rule('{RuleName}')/$links/_Box
```

When the \_Box.Name parameter is omitted, it is assumed that null is specified

### Method
POST

### Request query
| Query name | Summary | Valid values | Required | Remarks |
|:--|:--|:--|:--|:--|
| p_cookie_peer | cookie authentication value | cookie authentication value returned from the server at the time of authentication | No | valid only when there is no specification of the authorization header | specify when using cookie authentication information |

### Request Header
| Header name | overview | effective value | required | remarks |
|:--|:--|:--|:--|:--|
| X-HTTP-Method-Override | method override function | optional | No | If you specify this value when requesting with the POST method, the specified value will be used as a method. |
| X-Override | header override function | $ {overwrite header name}: $ {value} | No | overwrites the value of normal HTTP header. To overwrite multiple headers, specify multiple X-Override headers. |
| X-Personium-RequestKey |RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
| Authorization | Specify authentication information in OAuth 2.0 format | Bearer {AccessToken} | No | * Authentication token acquired with the authentication token acquisition API Token |
| Content-Type | Specify the format of the request body | application / json | No | treat it as [application / json] when omitted |
| Accept | Specify the response body format | application / json | No | treat as [application / json] when omitted |
### Request body
#### Format
JSON

| Item name | overview | effective value | required | remarks |
|:--|:--|:--|:--|:--|
| uri | URI of the OData resource to be linked | Number of digits: 1 to 1024 | Follow the URI format <br> scheme: http / https / urn | Yes ||

### Request body sample
```JSON
{"uri":"https://cell1.unit1.example/__ctl/Box(Name='box2')"}
```

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
curl  "https://cell1.unit1.example/__ctl/Rule('rule1')/\$links/_Box" -X POST -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d "{\"uri\":\"https://cell1.unit1.example/__ctl/Box('box2')\"}"
```
