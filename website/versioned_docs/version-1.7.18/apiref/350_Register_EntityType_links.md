---
id: version-1.7.18-350_Register_EntityType_links
title: Link other objects with EntityType
sidebar_label: Link other objects with EntityType
original_id: 350_Register_EntityType_links
---

## Overview

Register $links information of EntityType

### Required Privileges

alter-schema


## Request

### Request URL

```
EntityType
{CellURL}{BoxName}/{OdataCollecitonPath}/$metadata/EntityType(Name='{EntityTypeName}')/$links/_AssociationEnd
AssociationEnd
{CellURL}{BoxName}/{OdataCollecitonPath}/$metadata/AssociationEnd(Name='{AssociationEndName}',
 _EntityType.Name='{EntityTypeName}')/$links/_AssociationEnd
```

### Request Method

POST

### Request Query

None

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Accept|Specifies the response body format|application/json|No|[application/json] by default|

### Request Body

|Item Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|uri|Link to AssociationEnd uri|Present AssociationEnd|Yes||

### Request Sample

```JSON
{"uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata
/AssociationEnd(Name='association-end1',_EntityType.Name=null)"}
```


## Response

### Response Code

204

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|DataServiceVersion|Version information of ODataProtocol|Return only when AssociationEnd can be created successfully<br>Operation confirmed|

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

EntityType
```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata/EntityType(Name='entity-type1')\
/$links/_AssociationEnd" -X POST -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json' \
-d '{"uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata/AssociationEnd\
(Name='association-end1',_EntityType.Name=null)"}'

```

AssociationEnd
```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$metadata/AssociationEnd\
(Name='association-end2',_EntityType.Name='entity-type2')/$links/_AssociationEnd" -X POST -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '{"uri": "https://cell1.unit1.example/box1/odata-collection1/$metadata/AssociationEnd\
(Name='association-end3',_EntityType.Name='entity-type3')"}'
```


