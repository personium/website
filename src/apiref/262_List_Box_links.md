---
id: 262_List_Box_links
title: Retrieve links list from Box to other objects
sidebar_label: Retrieve links list from Box to other objects
---

## Overview

List OData resources associated with Box  
You can specify the following OData resources  

* Role
* Relation
* Rule

### Required Privileges
|Link Object|Required Privileges|
|:-|:-|
|Role|box-read<br>auth-read|
|Relation|box-read<br>social-read|
|Rule|box-read<br>rule-read|


### Restrictions

* Accept in the request header is ignored
* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body


## Request

### Request URL

#### link with Role

```
{CellURL}__ctl/Box(Name='{BoxName}',Schema='{SchemaURL}')/$links/_Role
```

or 

```
{CellURL}__ctl/Box(Name='{BoxName}')/$links/_Role
```

or 

```
{CellURL}__ctl/Box('{BoxName}')/$links/_Role
```

#### link with Relation

```
{CellURL}__ctl/Box(Name='{BoxName}',Schema='{SchemaURL}')/$links/_Relation
```

or 

```
{CellURL}__ctl/Box(Name='{BoxName}')/$links/_Relation
```

or 

```
{CellURL}__ctl/Box('{BoxName}')/$links/_Relation
```
#### link with Rule
```
{CellURL}__ctl/Box(Name='{BoxName}',Schema='{SchemaURL}')/$links/_Rule
```
or 

```
{CellURL}__ctl/Box(Name='{BoxName}')/$links/_Rule
```
or 

```
{CellURL}__ctl/Box('{BoxName}')/$links/_Rule
```

If the Schema is omitted, it is assumed that null is specified

### Request Method

GET

### Request Query

The following query parameters are available

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

<!---
[$select  Query](406_Select_Query.md)

[$expand  Query](405_Expand_Query.md)

[$format  Query](404_Format_Query.md)

[$filter  Query](403_Filter_Query.md)

[$inlinecount  Query](407_Inlinecount_Query.md)

[$orderby  Query](400_Orderby_Query.md)
-->

[$top  Query](401_Top_Query.md)

[$skip  Query](402_Skip_Query.md)

<!---
[Full-text Search (q) Query](408_Full_Text_Search_Query.md)
-->

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

None


## Response

### Response Code

200

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|DataServiceVersion|OData version||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

|Object|Item Name|Data Type|Notes|
|:--|:--|:--|:--|
|Root|d|object|Object{1}|
|{1}|results|array|Array object {2}|
|{2}|uri|string|URI of the linked OData resource|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```JSON
{
  "d": {
    "results": [
      {
        "uri": "https://cell1.unit1.example/__ctl/Role(Name='role1',_Box.Name='box1')"
      }
    ]
  }
}
```


## cURL Command

```sh
curl "https://cell1.unit1.example/__ctl/Box('box1')/\$links/_Role" -X GET -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

