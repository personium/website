---
id: 2A2_List_Rule
title: Retrieve List of Rule
sidebar_label: Retrieve List of Rule
---
## Overview
Obtain a list of existing Rule information

### Required Permissions
rule-read

### Limitations
* OData restriction
* Accept of request header is ignored
* Treat all Content-Type of the request header as application / json
* Accept only JSON format for request body
* Content-Type of the response header supports only application / json, and the response body is JSON format
* $ format query option ignored

## request
### Request URL
```
{CellURL}__ctl/Rule
```
### Method
GET

### Request query
The following query parameters are available.

| Query name | Summary | Valid values | Required | Remarks |
|:--|:--|:--|:--|:--|
| p_cookie_peer | cookie authentication value | cookie authentication value returned from the server at the time of authentication | No | valid only when there is no specification of the authorization header | specify when using cookie authentication information |

[$select query](406_Select_Query.md)

[$expand query](405_Expand_Query.md)

[$format query](404_Format_Query.md)

[$filter query](403_Filter_Query.md)

[$inlinecount query](407_Inlinecount_Query.md)

[$orderby query](400_Orderby_Query.md)

[$top query](401_Top_Query.md)

[$skip query](402_Skip_Query.md)

[Full Text Search (q) Query](408_Full_Text_Search_Query.md)

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
200
### Response header
| Header name | Overview | Remarks |
|:--|:--|:--|
| Access-Control-Allow-Origin | Cross-domain communication permission header | Return value is fixed as "*"
| X-Personium-Version | Execution version of API | API version processed request |
### OData response header

| Header name | Overview | Remarks |
|:--|:--|:--|
| Content-Type | Format of data to be returned ||
| DataServiceVersion | OData version ||
### Response body
The response is a JSON object, and the correspondence between the key (name) and type defined in the object (subobject) and the value are as follows.

| Object | item name | type | remarks |
|:--|:--|:--|:--|
| Route | d | object | object {1} |
| {1} | results | array | Array of objects {2}
| {2} | __metadata | object | object {3} |
| {3} | uri | string | URL to created resource |
| {3} | etag | string | Etag value |
| {2} | __published | string | creation date (UNIX time) |
| {2} | __updated | string | Update date (UNIX time) |
| {1} | __count | string | $ inlinecount number of results obtained by query |
### Rule specific response body
| Object | Item name | Data Type | Remarks |
|:--|:--|:--|:--|
| {3} | type | string | CellCtl.Rule |
| {2} | Name | string | Rule name |
| {2} | _Box.Name | string | Box name of relation |
| {2} | EventExternal | boolean ||
| {2} | EventSubject | string ||
| {2} | EventType | string ||
| {2} | EventObject | string ||
| {2} | EventInfo | string ||
| {2} | Action | string ||
| {2} | TargetUrl | string ||

### Error message list
[Error message list](004_Error_Messages.md) is referred to

### Response sample
```JSON
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/Rule(Name='rule1',_Box.Name='box1')",
          "etag": "W/\"1-1486368212581\"",
          "type": "CellCtl.Rule"
        },
        "Name": "rule1",
        "_Box.Name": "box1",
        "EventExternal": true,
        "EventSubject": null,
        "EventType": null,
        "EventObject": null,
        "EventInfo": null,
        "Action": "log",
        "TargetUrl": null,
        "__published": "/Date(1486368212581)/",
        "__updated": "/Date(1486368212581)/",
        "_Box": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Rule(Name='rule1',_Box.Name='box1')/_Box"
          }
        }
      },
      {
        "__metadata": {
          "uri": "https://cell1.unit1.example/__ctl/Rule(Name='rule2',_Box.Name='box2')",
          "etag": "W/\"1-1486461000154\"",
          "type": "CellCtl.Rule"
        },
        "Name": "rule2",
        "_Box.Name": "box2",
        "EventExternal": true,
        "EventSubject": null,
        "EventType": null,
        "EventObject": null,
        "EventInfo": null,
        "Action": "log",
        "TargetUrl": null,
        "__published": "/Date(1486461000154)/",
        "__updated": "/Date(1486461000154)/",
        "_Box": {
          "__deferred": {
            "uri": "https://cell1.unit1.example/__ctl/Rule(Name='rule2',_Box.Name='box2')/_Box"
          }
        }
      }
    ]
  }
}
```
## cURL Sample

```sh
curl "https://cell1.unit1.example/__ctl/Rule" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

