---
id: version-1.7.21-505_Get_Property_Snapshot_Cell
title: Retrieve Cell snapshot file setting
sidebar_label: Retrieve Cell snapshot file setting
original_id: 505_Get_Property_Snapshot_Cell
---

## Overview

Get Cell snapshot file property.

### Required Privileges

root

### Restrictions

* A function that specifies properties to be returned in the response body(Become current allprop)


## Request

### Request URL

```
{CellURL}__snapshot
```

or

```
{CellURL}__snapshot/{FileName}
```

### Request Method

PROPFIND

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|Specifying this value in a request with the POST method indicates that the specified value is used as the method|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|The normal HTTP header value is overwritten. Specify multiple X-Override headers for the overwriting of multiple headers|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Depth|To get the hierarchy of a resource|0:The target resource itself <br>1:Gets target and resources directly under the target|Yes||

### Request Body

Namespace

|URI|Overview|Reference prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

Structure of XML

The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|propfind|D:|Element|Represents the root element of propfind and allprop is a child||
|allprop|D:|Element|Represent setting to retrieve all properties|allprop : get all properties<br>Even if the request body is empty, treat it as allprop<br>Elements other than allprop are not supported|

DTD notation

```dtd
<!ELEMENT propfind (allprop) >
<!ELEMENT allprop ENPTY >
```

### Request Sample

```xml
<?xml version="1.0" encoding="utf-8"?>
<D:propfind xmlns:D="DAV:">
  <D:allprop/>
</D:propfind>
```


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|207|Multi-Status|Success|

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

### Response Body

Namespace

|URI|Overview|Reference prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|
|urn&#58;x-personium:xmlns|Personium namespace|p:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

Structure of XML

The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|multistatus|D:|Element|Represents the route of multistatus and one or more responses are children||
|response|D:|Element|Represents a response to resource acquisition, href and propstat are children||
|href|D:|Element|Resource url||
|propstat|D:|Element|Represents property information of a resource, status and prop are children||
|status|D:|Element|Represents the response code of resource acquisition||
|prop|D:|Element|Property detailed information, creationdate, resourcetype, acl, and proppatch setting values are children||
|creationdate|D:|Element|Resource creation time||
|getcontentlength|D:|Element|Resource size|Resource is only file|
|getcontenttype|D:|Element|Contenttype of resources|Resource is only file|
|getlastmodified|D:|Element|Resource update time||
|resourcetype|D:|Element|Represents the type of the resource. <br>If collection is a child or child is empty||
|collection|D:|Element|Represents that the type of resource is a collection|Displays, if resource is collection|
|acl|D:|Element|ACL setting set for resource|ACL Element See the [ Cell Level Access Control Settings API ](289_Cell_ACL.md) for content below|
|base|xml:|attribute|ACL Privilege BaseURL|When PROPFIND to Cell, default box ("__") resource URL|

DTD notation

Namespace D:

```dtd
<!ELEMENT multistatus (response*)>
<!ELEMENT response (href, propstat)>
<!ELEMENT href (#PCDATA)>
<!ELEMENT propstat (status, prop)>
<!ELEMENT status (#PCDATA)>
<!ELEMENT prop (creationdate, resourcetype, ANY)>
<!ELEMENT creationdate (#PCDATA)>
<!ELEMENT getcontentlength (#PCDATA)>
<!ELEMENT getcontenttype (#PCDATA)>
<!ELEMENT getlastmodified (#PCDATA)>
<!ELEMENT resourcetype ((collection or EMPTY))>
<!ELEMENT collection EMPTY>
<!ELEMENT acl (ace*)>
```

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```xml
<multistatus xmlns="DAV:">
  <response>
    <href>https://cell1.unit1.example/__snapshot/CellExport_2017_01.zip</href>
    <propstat>
      <prop>
        <creationdate>2017-02-15T01:52:34.635+0000</creationdate>
        <getcontentlength>2000000</getcontentlength>
        <getcontenttype>application/zip</getcontenttype>
        <getlastmodified>Wed, 15 Feb 2017 01:52:34 GMT</getlastmodified>
        <resourcetype/>
        <acl xmlns:p="urn:x-personium:xmlns"/>
      </prop>
      <status>HTTP/1.1 200 OK</status>
    </propstat>
  </response>
</multistatus>
```


## cURL Sample

```sh
curl "https://cell1.unit1.example/__snapshot/CellExport_2017_01.zip" -X PROPFIND -i  \
-H 'Depth:0' -H 'Authorization: Bearer {AccessToken}' -d '<?xml version="1.0" \
encoding="utf-8"?><D:propfind xmlns:D="DAV:"><D:allprop/></D:propfind>'
```


