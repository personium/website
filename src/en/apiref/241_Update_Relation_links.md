---
id: 241_Update_Relation_links
title: Relation\_$links update
sidebar_label: Relation\_$links update
---

## Overview

Update OData resources associated with Relation<br>You can specify the following OData resources

* Box
* ExtCell
* ExtRole
* Role

### Restrictions

* Accept in the request header is ignored
* Always handles Content-Type in the request header as application/json
* Only accepts the request body in the JSON format
* Only application/json is supported for Content-Type in the request header and the JSON format for the response body
* $formatQuery options ignored


## Request

### Request URL

#### Correlating with Box

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_Box('{BoxName}')
```

#### Correlating with ExtCell

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_ExtCell('{ExtCellURL}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtCell('{ExtCellURL}')
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtCell('{ExtCellURL}')
```

#### Linking with ExtRole

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}'
,_Relation.Name='{RelationName}',_Relation._Box.Name='{BoxName}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}',_Relation.Name=
'{RelationName}',_Relation._Box.Name='{BoxName}')
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}',_Relation.Name=
'{RelationName}',_Relation._Box.Name='{BoxName}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_ExtRole(ExtRole=
'{ExtRoleURL}',_Relation.Name='{RelationName}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}',_Relation.Name=
'{RelationName}')
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}',_Relation.Name=
'{RelationName}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_ExtRole(ExtRole=
'{ExtRoleURL}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}')
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtRole(ExtRole='{ExtRoleURL}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_ExtRole('{ExtRoleURL}')
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_ExtRole('{ExtRoleURL}')
```

#### Correlating with the Role

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_Role(Name='{RoleName}'
,_Box.Name='{BoxName}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_Role(Name='{RoleName}',_Box.Name='{BoxName}')
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_Role(Name='{RoleName}',_Box.Name='{BoxName}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_Role(Name='{RoleName}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_Role(Name='{RoleName}')
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_Role(Name='{RoleName}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}',_Box.Name='{BoxName}')/$links/_Role('{RoleName}')
```

or

```
{CellURL}__ctl/Relation(Name='{RelationName}')/$links/_Role('{RoleName}')
```

or

```
{CellURL}__ctl/Relation('{RelationName}')/$links/_Role('{RoleName}')
```

If the \_Box.Name, \_Relation.Name, \_Relation.\_Box.Name parameter is omitted, it is assumed that null is specified  
\* The ExCel key specifies the URL-encoded character string.

### Request Method

PUT

### Request Query

None

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/json|No|[application/json] by default|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|
|If-Match|Specifies the target ETag value|ETag value|No|[*] by default|

### Request Body

#### Format

JSON

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|uri|URI of the OData resource to be linked|Number of digits: 1-1024<br>Follow URI format<br>scheme:http / https / urn|Yes||

### Request Sample

```JSON
{"uri":"https://cell1.unit1.example/__ctl/Box('box3')"}
```


## Response

### Response Code

204

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|DataServiceVersion|OData version||
|ETag|Resource version information||

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/__ctl/Relation(Name='relation1',_Box.Name='box1')\
/$links/_Box('box2')" -X PUT -i -H 'If-Match:*' \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '{"uri":"https://cell1.unit1.example/__ctl/Box('box3')"}'
```

