# CORS (Cross Origin Resource Sharing) Support

## Overview

All API of Prsonium are empowered to make cross-origin requests to resources; they are based on CORS (Cross Origin Resource Sharing) principle though with some exceptions.  
Specifically, if there isno descriptor for the particular exception, based on the request all API endpoint will return the response header like below

1.  Access-Control-Allow-Origin
2.  Access-Control-Allow-Methods
3.  Access-Control-Allow-Headers

Thus for performing the HTTP asynchronous communication with the server, by Web browser installed script language such as JavaScript, using the XMLHttpRequest Level 2 will be possible.

### Return of Access-Control-Allow-Origin Response Header

In all the API, the value of Access-Control-Allow-Origin response header is returned as \*.  
The Access-Control-Allow-Origin header when set as \* indicates that a resource can be shared across various domains, In Personium such behavior allows access to the resources from all domains.  
Following is an example of the Access-Control-Allow-Origin response header.

```
Access-Control-Allow-Origin: *
```

### Response to the pre-flight requests from the browser

Following is the response of the pref. right requests from the browser, when you issue the request of the OPTIONS method in the API of all.

1.   Return of Access-Control-Allow-Methods response header
2.   Return of Access-Control-Allow-Headers response header

####  Return of Access-Control-Allow-Methods response header

When you issue the request of the OPTIONS method in the API of all, it returns the Access-Control-Allow-Methods response header.  
Contents of the Access-Control-Allow-Methods Responsive header will change as follows depending on the contents of the Authorization header and access control settings of the API.

|Condition|Result|
|:--|:--|
|The resources (read possible without Authorization header published)|It returns all the HTTP methods that the resource supports.|
|Private (non-public) OPTIONS request without the Authorization header to the resource|It returns all the HTTP methods that the Personium can support.|
|OPTIONS request to the private resources of a valid * Authorization header with|It returns all the HTTP methods that the resource supports.|

The request Authorization header, can sometimes generate following errors depending on the contents of the header.

1.   401: The content of the Authorization header is invalid, such as if the value of token happens to be incorrect .
2.   Indicates that the server can be reached and understood the request, but refuses to take any further action. Request is not accepted on account of the access denied to the request. For example, Reading is not allowed.

It returns the request method that is allowed inside the request URL.  
Following is an example of the Access-Control-Allow-Methods response header.

```
Access-Control-Allow-Methods: GET, OPTIONS
```

####  Return of Access-Control-Allow-Headers response header

In all the APIs, if you specify the Access-Control-Request-Headers in the request header, it returns the Access-Control-Allow-Headers.  
Following is an example of the response header if you specify a "sample" in the Access-Control-Request-Headers.

```
Access-Control-Allow-Headers: sample
```

### Reference

http://www.w3.org/TR/cors/

