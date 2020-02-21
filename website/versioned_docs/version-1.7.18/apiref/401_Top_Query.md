---
id: version-1.7.18-401_Top_Query
title: $top Query
sidebar_label: $top Query
original_id: 401_Top_Query
---

## Overview

By specifying an integer value in the $top query, it is possible to limit the number of data listings to be acquired  
If the number of registered data is less than the number of acquired data, all data is acquired  
If the number of registered data exceeds the number of acquisitions, acquire from the beginning of the registered data up to the number of acquisitions  
Because the data obtained by the $top query is not sorted, you need to specify a sort condition such as a $ orderby query

\*If you specify anything other than an integer value in $top, return "400 Bad Request"

## Request Query

```
$top={number}
```

|Value|Overview|Effective Value|Notes|
|:--|:--|:--|:--|
|{number}|Specify the number of entities included in the returned feed|Half size numeric 0-10000 (default: 25) <br> $expand 0-100 (default: 25) when query is specified||

## cURL Command

Example: When acquiring 10 cells:

```sh
curl "https://unit1.example/__ctl/Cell?\$top=10" -X GET -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json'
```

### Restrictions

* Considering processing performance, use with the $skip query  
    In this case, the recommended value of the $top query is 50 or less

