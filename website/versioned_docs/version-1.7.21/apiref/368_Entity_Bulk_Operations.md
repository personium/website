---
id: version-1.7.21-368_Entity_Bulk_Operations
title: Entity collective operation($batch)
sidebar_label: Entity collective operation($batch)
original_id: 368_Entity_Bulk_Operations
---

## Overview

Perform a batch operation such as list acquisition, single acquisition, registration, update, and deletion for ODataEntity

### Required Privileges

* Retrieve list / Retrieve one case  
    read
* Register / Update / Delete  
    write

### Restrictions

* $batch Restriction
    * "GET" request query is not supported
    * When list acquisition is executed, return 10 cases at random
    * "GET" via NavigationProperty is not supported
    * $links "PUT" "GET" "DELETE" is not supported (returns 501)


## Request

### Request URL

```
{CellURL}{BoxName}/{ODataCollecitonName}/$batch
```

|Path|Overview|
|:--|:--|
|{CellName}|Cell Name|
|{BoxName}|Box Name|
|{ODataCollecitonName}|Collection Name|

### Request Method

POST

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|*The authentication token is a token acquired by the authentication token acquisition API Not tested|
|Content-Type|Specifies the request body format|multipart / mixed; boundary = {Boundary}|Yes|When omitted, treat it as [multipart/mixed]  Characters that can be used for {Boundary}: alphabetic lower case '()+_,-./:=?<br>Not compatible|

### Request Body

Specify batch process content as request body in MIME multipart data format  
Up to 1,000 batch processes can be handled at maximum  
Batch processing includes "query operation" for context acquisition and "change set" for context registration, update, and deletion  
Describe how to describe request parameters below

```
(1)     --{Boundary string}
(2)     "query operation" or "change set"
(3)     --{Boundary string}
(4)     "query operation" or "change set"
(5)     --{Boundary string}--

(1) Specify the start boundary string "- {Boundary string}"
(2) Specify "query operation" or "change set"
(3) (4)Multiple specifications become possible by separating the request with the boundary string "- {Boundary string}"
(5) Specify the termination boundary string "- {Boundary string}"
```

* Query Operation  
    Retrieve the specified context  
    The description method of the query operation will be explained below  
    \*"GET" request query is not supported

```
(1)     Content-Type: application/http
(2)     Content-Transfer-Encoding:binary
(3)
(4)     GET :path
(5)     :request_header

(1) Specify Content-Type in application/http
(2) Specify Content-Transfer-Encoding in binary
(3) Specify an empty line
(4) Specify request method "GET" and path (: path)
    :path, specify the path for entity information acquisition
    For details, refer to "Request URI" of "Entity Acquisition"
(5) : Specify request header for :request_header
    Request header can be specified without specification, or one or more can be specified
```

* Change Set  
    Register / Update / Delete the specified context  
    Specify processing contents of registration, pdate and deletion with MIME multipart data  
    Describe how to describe the change set below

```
(1)     Content-Type: multipart/mixed; boundary={Change set Boundary string}
(2)     Content-Length: XXX
(3)
(4)     --{Change set Boundary string}
(5)     Content-Type: application/http
(6)     Content-Transfer-Encoding: binary
(7)
(8)     :method :path HTTP/1.1
(9)     :request_header
(10)
(11)    :data
(12)
(13)       --{Change set Boundary string}--

(1) Specify Content-Type with multipart/mixed
    See [Request header] for the character type that can be used for {Change set Boundary string}
(2) Specify Content-Length XXX specifies the contents-length of the change set
(3) Specify an empty line
(4) Start Changeset Boundary String Specify "- {Change set Boundary string}"
(5) Specify Content-Type in application/http
(6) Specify Content-Transfer-Encoding in binary
(7) Specify an empty line
(8) Specify the request method (: method), the path (: path), and the HTTP version "HTTP/1.1"
    :method specifies either request method "POST" "PUT" "DELETE"
    :path, specify the path of entity registration, update, and deletion processing
(9) Specify request header for :request_header
    Request header can be specified without specification, or one or more can be specified
(10) Specify an empty line
(11) In the case of the request method "POST" "PUT", specify the data to be registered / updated in :data in the JSON
    format
(12) In case of the request method "POST" "PUT", specify a blank line
(13) End Changeset Boundary String Specify "- {Change set Boundary string} -"
    From the change set boundary string to the change set boundary character string becomes one request information, 
    and multiple requests can be specified by delimiting the request with the change set boundary character string
```

### Request Path

* { EntitySet name}
* { EntitySet name}('{\_\_id}')
* { EntitySet name}('{\_\_id}')/{NavigationProperty name}
* { EntitySet name}('{\_\_id}')/$links/{NavigationProperty name}

### Request Method

POST, GET, PUT, DELETE

### Request Queries

Not compatible

### Request Header

Follow the specifications of user data

### Request Body

Follow the specifications of user data

### Request Sample

The following shows an example of a request when acquiring, registering, updating and deleting a context with the following flow

* Retrieve "ID: 0000"
* Registered as "ID: 0000, Name: John Smith"
* Updated with "ID: 0000, familyName: Smith, givenName: John"
* Retrieve "ID: 0000"
* Register "ID: 0001, Name: John log" via NavigationProperty
* Delete "ID: 0001"
* Delete "ID: 0000"

```
--batch_31e84e14-28b9-4741-903f-b955f2a1b853
Content-Type: application/http
Content-Transfer-Encoding:binary

GET entity-type1('0000')
Accept-Encoding: gzip
Accept: application/json
Content-Length: 0
--batch_31e84e14-28b9-4741-903f-b955f2a1b853
Content-Type: multipart/mixed; boundary=changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159
Content-Length: 608

--changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159
Content-Type: application/http
Content-Transfer-Encoding: binary

POST entity-type1
Content-Type: application/json
Content-Length: 41

{"__id":"0000","Name":"John Smith"}

--changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159
Content-Type: application/http
Content-Transfer-Encoding: binary

PUT entity-type1('0000')
Content-Type: application/json
Content-Length: 87
If-Match: *

{"__id":"0000","Name":"John Smith","familyName":"Smith ","givenName":"John"}

--changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159--
--batch_31e84e14-28b9-4741-903f-b955f2a1b853
Content-Type: application/http
Content-Transfer-Encoding:binary

GET entity-type1('0000')
Accept-Encoding: gzip
Accept: application/json
Content-Length: 0
--batch_31e84e14-28b9-4741-903f-b955f2a1b853
Content-Type: multipart/mixed; boundary=changeset_d4883767-a06e-4632-9608-ae952b443dfc
Content-Length: 686

--changeset_d4883767-a06e-4632-9608-ae952b443dfc
Content-Type: application/http
Content-Transfer-Encoding: binary

POST entity-type1('0001')/_log
Content-Type: application/json
Content-Length: 37

{"__id":"0001","Name":"John log"}

--changeset_d4883767-a06e-4632-9608-ae952b443dfc
Content-Type: application/http
Content-Transfer-Encoding: binary

DELETE entity-type1('0001')/_log
Content-Length: 0
If-Match: *
--changeset_d4883767-a06e-4632-9608-ae952b443dfc
Content-Type: application/http
Content-Transfer-Encoding: binary

DELETE entity-type1('0000')
Content-Length: 0
If-Match: *
--changeset_d4883767-a06e-4632-9608-ae952b443dfc--
--batch_31e84e14-28b9-4741-903f-b955f2a1b853--
```


## Response

### Response Code

202

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned|When $ batch processing succeeded normally: multipart/mixed; boundary={Boundary}|
|DataServiceVersion|OData version information|Return only when Entity can be created successfully|

### Response Body

Response sample reference

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

The following shows an example of the response when executing the above example of the request parameter

* Retrieve "ID: 0000"
* Registered as "ID: 0000, Name: John Smith"
* Updated with "ID: 0000, familyName: Smith, givenName: John"
* Retrieve "ID: 0000"
* Register "ID: 0001, Name: John log" via NavigationProperty
* Delete "ID: 0001"
* Delete "ID: 0000"

```
--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX
Content-Type: application/http

HTTP/1.1 404 Not Found
Content-Type: application/json
Content-Length: 48
DataServiceVersion: 2.0

{
  "error": {
    "code": "404",
    "message": "Not Found"
  }
}

--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX
Content-Type: multipart/mixed; boundary=changeset_qPJh1ATATNykjJT8ocPE5MJE3QzMBS19ljS

--changeset_qPJh1ATATNykjJT8ocPE5MJE3QzMBS19ljS
Content-Type: application/http
Content-Transfer-Encoding: binary
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 425
DataServiceVersion: 2.0
Location: http://unit1.example:50280/api/context/xxx-ah,http%253A%252F%252FUnitFQDN%252Fds%252Fabc-web
/odata/user('0000')
{
  "d": {
    "Results": {
      "__metadata": {
        "uri": "http://unit1.example/api/context/xxx-ah,http%253A%252F%252FUnitFQDN%252Fds%252Fvet-web
/odata/user('0000')"
        "etag": "W/\"1-1488184348000\"",
        "type": "UserData.user",
      },
      "__id": "0000",
      "__published": "/Date(1488184348000)/",
      "__updated": "/Date(1488184348000)/",
      "name": "John Smith"
      }
    }
  }
}

--changeset_qPJh1ATATNykjJT8ocPE5MJE3QzMBS19ljS--
--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX
Content-Type: multipart/mixed; boundary=changeset_mry0iPNyKqKONtK237cBbGHUQhNgwIxlg70

--changeset_mry0iPNyKqKONtK237cBbGHUQhNgwIxlg70
Content-Type: application/http
Content-Transfer-Encoding: binary
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 0
DataServiceVersion: 2.0

--changeset_mry0iPNyKqKONtK237cBbGHUQhNgwIxlg70--
--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX
Content-Type: application/http

HTTP/1.1 200 OK
Content-Length: 457
ETag: W/"1-1488184348000"
DataServiceVersion: 2.0
Content-Type: application/json
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1('0000')"
        "etag": "W/\"1-1370248522812\"",
        "type": "UserData.user",
      },
      "__id": "0000",
      "__published": "/Date(1370248522812)/",
      "__updated": "/Date(1370248522812)/",
      "name": "John Smith",
      "_log": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('0000')/_log"
        }
      }
    }
  }
}

--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX
Content-Type: multipart/mixed; boundary=changeset_wtsoeMGaDT6vDVM8QooqoLGEH8s6nHcrh6C

--changeset_mry0iPNyKqKONtK237cBbGHUQhNgwIxlg70
Content-Type: application/http
Content-Transfer-Encoding: binary
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 0
DataServiceVersion: 2.0

--changeset_d4883767-a06e-4632-9608-ae952b443dfc
Content-Type: application/http
Content-Transfer-Encoding: binary
HTTP/1.1 204 No Content
Content-Type: application/json
Content-Length: 0
DataServiceVersion: 2.0

--changeset_wtsoeMGaDT6vDVM8QooqoLGEH8s6nHcrh6C
Content-Type: application/http
Content-Transfer-Encoding: binary
HTTP/1.1 204 No Content
Content-Type: application/json
Content-Length: 0
DataServiceVersion: 2.0
--changeset_wtsoeMGaDT6vDVM8QooqoLGEH8s6nHcrh6C--
--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX--
```


## cURL Command

curl command

```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$batch" -X POST -i -H \
'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Content-Type:multipart/mixed; boundary=\
batch_XAmu9BiJJLBa20sRWIq74jp2UlNAVueztqu' --data-binary @sample.txt
```

sample.txt

```
--batch_XAmu9BiJJLBa20sRWIq74jp2UlNAVueztqu
Content-Type: application/http
Content-Transfer-Encoding:binary

GET entity-type1('{100-1_20101108-111352093}')
Authorization: Bearer AA~PBDc...(snip)...FrTjA
--batch_XAmu9BiJJLBa20sRWIq74jp2UlNAVueztqu
Content-Type: multipart/mixed; boundary=changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159
Content-Length: 608

--changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159
Content-Type: application/http
Content-Transfer-Encoding: binary

POST entity-type1
Content-Type: application/json
Content-Length: 41

{"__id":"100","Name":"John Smith"}

--changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159--
--batch_XAmu9BiJJLBa20sRWIq74jp2UlNAVueztqu--
```


