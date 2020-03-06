---
id: version-1.7.21-400_Orderby_Query
title: $orderby Query
sidebar_label: $orderby Query
original_id: 400_Orderby_Query
---

## Overview

Use the $orderby query to sort search results when retrieving lists  
\*If you specify a property name that does not exist in $orderby, ignore the specified item

## Request Query

```
$orderby={propertyName} {option}, ...
```

\*{propertyName} {option} can be specified in comma-separated list

|Path|Overview|
|:--|:--|
|{PropertyName}|Property name to specify as the sort key|
|{Option}|Sort method<br>asc:ascending order<br>desc:descending order<br>default:asc|

## cURL Command

Example: To obtain cell information in descending order of cell name:

```sh
curl "https://unit1.example/__ctl/Cell?\$orderby=Name%20desc" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

## Operation details

* Sort order for null values  
    When ascending order is specified, null is sorted so that it becomes the end of the sorting result when both descending order is specified.  
    \*However, if you are using the minor version 0.19.9, sort according to the following rules.
* Sort for string type
    * asc  
        Null -> string
    * desc  
        String -> null
* Numeric
    * asc  
        Negative number -> null -> 0 -> None -> Positive number
    * desc  
        Positive number -> null -> 0 -> none -> Pegative number
* If you specify a property name that does not exist in $orderby, ignore the specified item
* If an array type property name is specified in $orderby, 400 error is returned

