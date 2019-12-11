# Delete Rule
## Overview
Delete registered Rule

### Required Permissions
rule

### Limitations
* OData restriction
* Accept of request header is ignored
* Treat all Content-Type of the request header as application / json
* Accept only JSON format for request body
* Content-Type of the response header supports only application / json, and the response body is JSON format
* $format query option ignored

## request
### Request URL
```
{CellURL}__ctl/Rule(Name='{RuleName}',_Box.Name='{BoxName}')
```
Alternatively,
```
{CellURL}__ctl/Rule(Name='{RuleName}')
```
Alternatively,
```
{CellURL}__ctl/Rule('{RuleName}')
```
When the \_Box.Name parameter is omitted, it is assumed that null is specified
### Method
DELETE

### Request query
| Query name | Summary | Valid values | Required | Remarks |
|:--|:--|:--|:--|:--|
| p_cookie_peer | cookie authentication value | cookie authentication value returned from the server at the time of authentication | No | valid only when there is no specification of the authorization header <br> specifying when using the authentication information of the cookie |
### Request Header
| Header name | overview | effective value | required | remarks |
|:--|:--|:--|:--|:--|
| X-HTTP-Method-Override | method override function | optional | No | If you specify this value when requesting with the POST method, the specified value will be used as a method. |
| X-Override | header override function | $ {overwrite header name}: $ {value} | No | overwrites the value of normal HTTP header. To overwrite multiple headers, specify multiple X-Override headers. |
| X-Personium-RequestKey |RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|

### OData Request Header
| Header name | overview | effective value | required | remarks |
|:--|:--|:--|:--|:--|
| Authorization | Specify authentication information in OAuth 2.0 format | Bearer {AccessToken} | No | * Authentication token acquired with the authentication token acquisition API Token |
### OData Registration Request Header
| Header name | overview | effective value | required | remarks |
|:--|:--|:--|:--|:--|
| Content-Type | Specify the format of the request body | application / json | No | treat it as [application / json] when omitted |
| Accept | Specify the response body format | application / json | No | treat as [application / json] when omitted |
### Request body
None

## Response
### Status code
204
### Response header
None
### Response body
None
### Error message list
[Error message list](004_Error_Messages.md) is referred to

### Response sample
None


## cURL Sample

```sh
curl "https://cell1.unit1.example/__ctl/Rule(Name='rule1',_Box.Name='box1')" -X DELETE -i \
-H 'If-Match: *' -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

