---
id: 2A6_List_Rule_links
title: Retrieve links list from Rule to other objects
sidebar_label: Retrieve links list from Rule to other objects
---
## Overview
Get a list of OData resources associated with Rule  
You can specify the following OData resources  

* Box

### Required Privileges
|Link Object|Required Privileges|
|:-|:-|
|Box|rule-read<br>box-read|

### Limitations
* Content-Type of the response header supports only application / json, and the response body is JSON format


## request
### Request URL
```
{CellURL}__ctl/Rule(Name='{RuleName}',_Box.Name='{BoxName}')/$links/_Box
```

### Method
GET
### Request query
The following query parameters are available.

| Query name | Summary | Valid values | Required | Remarks |
|:--|:--|:--|:--|:--|
| p_cookie_peer | cookie authentication value | cookie authentication value returned from the server at the time of authentication | x | valid only when there is no specification of the authorization header <br> specifying when using the authentication information of the cookie |

<!---
[$select query](406_Select_Query.md)

[$expand query](405_Expand_Query.md)

[$format query](404_Format_Query.md)

[$filter query](403_Filter_Query.md)

[$inlinecount query](407_Inlinecount_Query.md)

[$orderby query](400_Orderby_Query.md)
-->

[$top query](401_Top_Query.md)

[$skip query](402_Skip_Query.md)

<!---
[Full Text Search (q) Query](408_Full_Text_Search_Query.md)
-->

### Request Header
| Header name | overview | effective value | required | remarks |
|:--|:--|:--|:--|:--|
| X-HTTP-Method-Override | method override function | optional | No | If you specify this value when requesting with the POST method, the specified value will be used as a method. |
| X-Override | header override function | ${overwrite header name}: ${value} | No | overwrites the value of normal HTTP header. To overwrite multiple headers, specify multiple X-Override headers. |
| X-Personium-RequestKey |RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
| Authorization | Specify authentication information in OAuth 2.0 format | Bearer {AccessToken} | No | * Authentication token acquired with the authentication token acquisition API Token |
| Accept | Specify the response body format | application / json | No | treat as [application / json] when omitted |
### Request body
None

### Request sample
None


## Response
### Status code
200

### Response header

| Header name | Overview | Remarks |
|:--|:--|:--|
| Content-Type | Format of data to be returned ||
| DataServiceVersion | OData version ||
| Access-Control-Allow-Origin | Cross-domain communication permission header | Return value is fixed as "*"
| X-Personium-Version | Execution version of API | API version processed request |

### Response body

| Object | Item name | Data Type | Remarks |
|:--|:--|:--|:--|
| Route | d | object | object {1} |
| {1} | results | array | Array of objects {2}
| {2} | uri | string | URL to linked OData resource |
### Error message list
[Error message list](004_Error_Messages.md) is referred to

### Response sample
```JSON
{
  "d": {
    "results": [
      {
        "uri": "https://cell1.unit1.example/__ctl/Box(Name='box1')"
      }
    ]
  }
}
```

## cURL Sample

```sh
curl "https://cell1.unit1.example/__ctl/Rule(Name='rule1',_Box.Name='box1')/\$links/_Box" -X GET \
-i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```
