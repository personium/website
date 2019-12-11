---
id: 405_Expand_Query
title: $expand Query
sidebar_label: $expand Query
---

## Overview

By specifying the name of NavigationProperty in the $expand query, it is possible to expand related information and acquire it.  
The expansion of related information at the time of list acquisition is expanded up to 100 cases.  
Deployment of related information at the time of acquiring one case will expand up to 10000 cases.  
The sort order of related data acquired by $expand is as follows.

|Relation|Sort conditions|order|
|:--|:--|:--|
|0 .. 1:0 .. 1|Entity creation date and time of the navigation property to be expanded|Descending order|
|0 .. 1: *|Entity creation date and time of the navigation property to be expanded|Descending order|
|*: 0 .. 1|Entity creation date and time of the navigation property to be expanded|Descending order|
|*: *|Link information creation date and time with the navigation property to be expanded|Descending order|

\*When Multiplicity is "1", the sort result is the same as "0..1".

## Request Query

```
$expand={NavigationPropertyName}
```

|Path|Overview|
|:--|:--|
|{NavigationPropertyName}|Navigation property name to expand<br>To specify more than one, specify it with a comma separator|

\*If you specify a NavigationProperty name that does not exist in $expand, return "400 Bad Request"

#### Navigation property Specifiable number

You can specify up to 2 navigation properties when acquiring list  
You can specify up to 10 navigation properties when acquiring one case  
\*If you exceed the number of navigation properties that can be specified return "400 Bad Request"

## cURL Command

Expand and acquire information associated with navigation properties

```
curl "https://cell1.unit1.example/box1/odata-collection1/entity-type1\
('100-1_20101108-111352093')?\$expand={NavigationPropertyName}" -X GET -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA'\
 -H 'Accept: application/json'
```

### Restrictions

* Expansion of related information can be done in one level only
* Add \_\_count as an item in the related information list (not supported) to indicate whether the expanded related information has returned all cases

