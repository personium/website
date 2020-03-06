---
id: version-1.7.21-406_Select_Query
title: $select  Query
sidebar_label: $select  Query
original_id: 406_Select_Query
---

## Overview

When specifying the property to return, use the $ select query  
If omitted, return all the acquired properties  
However, the following properties are always returned without specifying them in $select

* \_\_id
* \_\_published
* \_\_updated
* \_\_metadata

\*If you specify a property name that does not exist in $select, ignore the specified item  
\*If the value of the Dynamic property specified by $select is null, you can not get the property value  
\*Specify the property name without enclosing it with "'" (single quote)

## Request Query

```
$select={propertyName}
```

\*When omitted, it is $select = *

|Path|Overview|
|:--|:--|
|{PropertyName}|Property name to return<br>To specify more than one, specify it with a comma separator|

## cURL Command

Example: When returning only Name property when acquiring Box list:

```sh
curl "https://cell1.unit1.example/__ctl/Box?\$select=Name" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

Example: When returning all the properties when acquiring the Box list:

```
curl "https://cell1.unit1.example/__ctl/Box?\$select=*" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```


