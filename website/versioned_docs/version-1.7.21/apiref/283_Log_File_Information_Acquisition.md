---
id: version-1.7.21-283_Log_File_Information_Acquisition
title: Retrieve Log File Information
sidebar_label: Retrieve Log File Information
original_id: 283_Log_File_Information_Acquisition
---

## Overview

Retrieve Event Log File Information  
If you exceed the maximum number of generations to hold rotate when the log file, the log file of the oldest is deleted.

### Required Privileges

log-read

### Restrictions

* Log output of the internal event is not supported, Log output configuration is not supported
* log file name"default.log"(fixed)
* Set rotate size: 50MB
* Configure the log output label to "info"(fixed)(output for all INFO, WARN, ERROR)
* The file name when rotated is default.log. {Timestamp}. {Timestamp} is numbered by the time when it was rotated.


## Request

### Request URL

#### Recent log file list

```
{CellURL}__log/current
```

#### Recent log file

```
{CellURL}__log/current/default.log
```

#### List of log file that is rotated

```
{CellURL}__log/archive
```

#### Log file that is rotated

```
{CellURL}__log/archive/default.log.{Timestamp}
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
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Depth|To get the hierarchy of a resource|0:Gets target resource only<br>1:Gets target and resources directly under the target|Yes||

### Request Body

None


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|207|Multi-Status|Success|

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||
|DataServiceVersion|OData Version|Return only when Entity can be successfully acquired|

### Response Body

Namespace

|Item Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned|D:|
|urn&#58;x-personium:xmlns|Personium namespace|p:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

#### Structure of XML

The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|multistatus|D:|Element|Represents the route of multistatus and one or more responses are children||
|response|D:|Element|Represents a response to resource acquisition, href and propstat are children||
|href|D:|Element|Resource url||
|propstat|D:|Element|Represents property information of a resource, status and prop are children||
|prop|D:|Element|Property detailed information, creationdate, resourcetype, acl, and proppatch setting values are children||
|creationdate|D:|Element|Resource creation time||
|getcontentlength|D:|Element|Resource size|Resource is only file|
|getcontenttype|p:|Element|Contenttype of resources|Resource is only file|
|getlastmodified|p:|Element|Resource update time||
|resourcetype|p:|Element|Represents the type of the resource. <br>Eventually the collection, OData service will vary, child will be empty||
|collection|p:|Element|Represents that the type of resource is a collection|Displays, if resource is collection|
|odata|p:|Element|Represents that the type of resource is a odata collection|Displays, if resource is odata collection|
|service|p:|Element|Represents that the type of resource is a service collection|Displays, if resource is service collection|
|acl|p:|Element|ACL setting set for resource|In order to acquire the ACL setting, acl-read authority for the target resource is required. For contents below the ACL element, refer to the [cell level access control setting API](289_Cell_ACL.md)|
|base|p:|Element|ACL Privilege BaseURL|When PROPFIND to Cell, default box ("__") resource URL|
|status|D:|Element|Represents the response code of resource acquisition||

#### DTD notation

Namespace: D:

```dtd
<!ELEMENT multistatus (response*)>
<!ELEMENT response (href, propstat)>
<!ELEMENT href (#PCDATA)>
<!ELEMENT propstat (status, prop)>
<!ELEMENT status (#PCDATA)>
<!ELEMENT prop (creationdate, resourcetype, acl, ANY)>
<!ELEMENT creationdate (#PCDATA)>
<!ELEMENT getcontentlength (#PCDATA)>
<!ELEMENT getcontenttype (#PCDATA)>
<!ELEMENT getlastmodified (#PCDATA)>
<!ELEMENT resourcetype ((collection, (odata or service) or EMPTY))>
<!ELEMENT collection EMPTY>
<!ELEMENT acl (ace*)>
```

Namespace:p:

```dtd
<!ELEMENT odata EMPTY>
<!ELEMENT service EMPTY>
```

Namespace: xml:

```dtd
<!ATTLIST acl base CDATA #IMPLIED>
```

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```xml
<multistatus xmlns="DAV:">
  <response>
    <href>https://cell1.unit1.example/__log/archive</href>
    <propstat>
      <prop>
        <creationdate>2017-02-03T01:27:31.093+0000</creationdate>
        <getlastmodified>Fri, 03 Feb 2017 01:27:31 GMT</getlastmodified>
        <resourcetype>
          <collection/>
        </resourcetype>
      </prop>
      <status>HTTP/1.1 200 OK</status>
    </propstat>
  </response>
</multistatus>
```


## cURL Command

```sh
curl "https://cell1.unit1.example/__log/archive" -X PROPFIND -i -H 'Depth:1' \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '<?xml version="1.0" encoding="utf-8"?><D:propfind xmlns:D="DAV:"><D:allprop/></D:propfind>'
```

