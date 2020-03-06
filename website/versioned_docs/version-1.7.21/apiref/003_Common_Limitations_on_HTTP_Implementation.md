---
id: version-1.7.21-003_Common_Limitations_on_HTTP_Implementation
title: Common Limitations on HTTP Implementation of Personium
sidebar_label: Common Limitations on HTTP Implementation of Personium
original_id: 003_Common_Limitations_on_HTTP_Implementation
---


## Request

### URL

Maximum Length: 50KByte  
\*URL Size = header size + (URL path size * 2) + (query size * 3)  
\*limit) IE7, 8 Many reference the browser is about 1Mbyte 2048byte, IE9 is other 5120byte,

### Request Header

The maximum size of each header: 4096 byte (whether or not including the length of the key is unknown)

#### Accept Encoding

Supports GZip

### Request Body

#### Transfer-Encoding

I have to respond to a request for chunked. (Unconfirmed)

#### Content-Encoding

It does not support is expected to respond to a request for gzip.

### Time-out

Time of 60 seconds from the start of the request, the server until you have received all of the request (unconfirmed)


## Response

### Response Header

|Header Name|Description|
|:--|:--|
|Transfer-Encoding|It always respond with chunked|
|Content-Encoding|If set to a valid value Accept-Encoding request header contains the value|
|Date|It returns the UTC time that the request has been accepted|

### Response Body

#### Size Limit

#### Transfer-Encoding

Support to chunked request

#### Content-Encoding

If you set the value of a valid request Accept-Encoding header is compressed and encoded in the form of its body.

