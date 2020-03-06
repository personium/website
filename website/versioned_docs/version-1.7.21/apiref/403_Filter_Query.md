---
id: version-1.7.21-403_Filter_Query
title: $filter Query
sidebar_label: $filter Query
original_id: 403_Filter_Query
---

## Overview

Use the $filter query to specify the search condition when retrieving the list

## Specifiable type

|Type|Description example|Notes|
|:--|:--|:--|
|Character string|'StringValue'||
|Numeric value|100||
|Boolean value|true<br>false||
|Date|datetime'2017-12-15T09:39:10'<br>datetimeoffset'2017-12-15T18:39:10+09:00'|"datetime" can not specify time zone offset.<br>If timezone offset is not specified, treat it as UTC.|

## Operator Support

|Operator|Meaning|Description example|Notes|
|:--|:--|:--|:--|
|eq|equal|$filter=itemKey eq 'searchValue'|Corresponds to character string, numeric value, boolean value, Date, null|
|ne|Negative Equal|$filter=itemKey ne 'searchValue'|Corresponds to character string, numeric value, boolean value, Date, null|
|gt|Greater than|$filter=itemKey gt 1000|Corresponds to character string, numeric value, Date|
|ge|Greater equal|$filter=itemKey ge 1000|Corresponds to character string, numeric value, Date|
|lt|Less than|$filter=itemKey lt 1000|Corresponds to character string, numeric value, Date|
|le|Less equal|$filter=itemKey le 1000|Corresponds to character string, numeric value, Date|
|and|AND|$filter=itemKey1 eq 'searchValue1' and itemKey2 eq 'searchValue2'||
|or|OR|$filter=itemKey1 eq 'searchValue1' or itemKey2 eq 'searchValue2'||
|()|Priority group|$filter=itemKey eq 'searchValue' or (itemKey gt 500 and itemKey lt 1500)|If parentheses are only one, parentheses are ignored|

## Support function

|Function|Overview|Example|Notes|
|:--|:--|:--|:--|
|startswith|Forward match|$filter=startswith(itemKey, 'searchValue')|Only for character string correspondence|

\*Partial match, backward match is not supported.

## Search specification by property type

### Edm.String

Convert keywords specified for search to string type and search

### Edm.Int32

An integer value or null can be specified  
If an integer value is specified as a string type, it is searched by converting it to a numeric type

### Edm.Single

It can specify integer, fractional value or null  
If it is a string type integer, if decimal value is specified convert it to decimal value and search

### Edm.Boolean

Only boolean values or null can be specified

### Edm.DateTime

Date or null can be specified.  
If an integer value is specified, it converts it to UNIX time and performs a search.

## Notices

\*URL encoding required for query specification  
\*Valid values of the property to be searched are half-size alphanumeric characters, - (hyphen), \_ (underscore) valid.  
\*If you want to include a single quote in the search string, you can specify a single quote as a search string by describing two single quotes"''"  
\*If a property name that does not exist in $ filter is specified, search is performed ignoring the property name  

## cURL Command

Example: When acquiring a cell whose cell name is sample:

```sh
curl "https://unit1.example/__ctl/Cell?\$filter=Name%20eq%20'sample'" -X GET -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```

