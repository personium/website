# Full-text Search (q) Query

## Overview

Use full-text search (q) query when specifying full-text search keyword when acquiring list  
Including complex type data, all values are searched

\*URL encoding required for query specification  
\*When specifying \_\_updated, \_published values, specify them by UNIX time(a number in parenthesis of "/Date()")  
\*Items in \_metadata are not subject to search

## Request Query

```
q={SearchKeyword}
```

|Item|Overview|Effective Value|Notes|
|:--|:--|:--|:--|
|{SearchKeyword}|Specify search string|Number of digits: 1-255 byte||

## Type to be searched

The data types to be searched are shown below

|Data type|Search target|Notes|
|:--|:--|:--|
|Edm.String|Yes||
|Edm.Boolean|Yes||
|Edm.Single|Yes||
|Edm.Int32|Yes||
|Edm.Double|Yes|Dynamic property only|
|Edm.DateTime|No||

## Search Specification

* Half space blank
    * Treat as delimiter
    * "(Double quote), it is not treated as one word
    * Example) The following specification searches for data including the keywords "Pochi" and "Tama"

        ```
        q=Pochi%20Tama
        q="Pochi%20Tama"
        ```

* Half size alphanumeric characters
    * Can not search for partial matches within keywords
    * Not distinguish between capital letters and small letters

* Double-byte character
    * Searchable for partial matches
    * Not distinguish between capital letters and small letters

## cURL Command

Example: When acquiring a cell list, when acquiring a cell that matches the keyword "sample":

```sh
curl "https://unit1.example/__ctl/Cell?q=sample" -X GET -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json'
```

