---
id: 2A3_Update_Rule
title: Update Rule
sidebar_label: Update Rule
---
## Overview
Update existing Rule information

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
PUT

### Request query
| Query name | Summary | Valid values | Required | Remarks |
|:--|:--|:--|:--|:--|
| p_cookie_peer | cookie authentication value | cookie authentication value returned from the server at the time of authentication | No | valid only when there is no specification of the authorization header <br> specifying when using the authentication information of the cookie |
### Request Header
| Header name | overview | effective value | required | remarks |
|:--|:--|:--|:--|:--|
| X-HTTP-Method-Override | method override function | optional | No | If you specify this value when requesting with the POST method, the specified value will be used as a method. |
| X-Override | header override function | $ {overwrite header name}: $ {value} | No | overwrites the value of normal HTTP header. To overwrite multiple headers, specify multiple X-Override headers. |
| X-Personium-RequestKey |RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|

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
#### Format

JSON  

| Item name | overview | effective value | required | remarks |
|:--|:--|:--|:--|:--|
| _Box.Name | Box name to which the rule should be attached | valid box name. A request not specifying this key or specifying a null value is interpreted as a Rule that is not associated with any Box.| No ||
| Name | Arbitrary name to identify the rule to be created | When linking to a Box, it is unique within the Box, and if it is not tied to the Box, it must be unique in the cell. When | No | is omitted, the uuid automatically allocates |
| EventType | Character string for forward match checking for the type of event that triggers a rule | For Evnet Type, the type is defined for internal events as a separate table (not created). For external events, you can specify any Type. | No ||
| EventSubject | Event Subject for Event Subject to Trigger Rule The string for matching check | Event Subject is basically the URL of Cell, so valid value is the exact match string. | No ||
| EventObject | Event Object's event object to trigger the rule String for forward match check | Event The value of object depends on the type of event. An arbitrary character string can be set, but the meaningful value depends on the event type. | No ||
| EventInfo | Event Info matching event check event for event that should trigger rule | Event info value depends on event type. An arbitrary character string can be set, but the meaningful value depends on the event type. | No ||
| EventExternal | Flag indicating whether the event to trigger the rule is an external event | Boolean. Set to true to detect external events. | No | default value false |
| Action | Action to be started when the event matches | Valid values are [Appendix](2A0_Create_Rule.md) | Yes ||
| TargetUrl | The value to be specified depends on the value of the concrete target URL | Action for the action. The rule is [attached table](2A0_Create_Rule.md) | No ||

### Request sample
```JSON
{"Name":"rule2", "EventExternal":true, "Action":"log"}
```
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
curl "https://cell1.unit1.example/__ctl/Rule('rule1')" -X PUT -i -H 'If-Match: *' -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '{"Name":"rule2", "EventExternal":true, "Action":"log"}'
```
