# Retrieve List of Log File

## Overview

Retrieve the list of log files under the specified URL

### Required Privileges

log-read

### Restrictions

Planned log output configuration is not yet supported.  Following fixed configuration is applied.

* log file name is "default.log".
* Log file is rotated when the size reaches a certain amount (50MB). 
* When rotated the file will be renamed to "default.log. {Timestamp}". {Timestamp} represents the time when the file is rotated.
* Only a certain number of archived logs are kept.  (12 generations)
* When the number of archived files exceeds the maximum, the oldest log file is automatically deleted.

|Action|Archived log file|Description|Notes|
|:--|:--|:--|:--|
|First Rotation|archive/<br>default.log.1402910774659|<br>Newly rotated file|<br>2014-06-16 18:26:14 +0900|
|2nd Rotation|archive/<br>default.log.1402910774659<br>default.log.1403910784659|<br>the preceding roteted file<br>Newly rotated file|<br>2014-06-16 18:26:14 +0900<br>2014-06-28 08:13:04 +0900|
|3rd Rotation|archive/<br>default.log.1402910774659<br>default.log.1403910784659<br>default.log.1403910784659|<br>the file before preceding file<br>the preceding roteted file<br>Newly rotated file|<br>2014-06-16 18:26:14 +0900<br>2014-06-28 08:13:04 +0900<br>2014-07-09 21:59:44 +0900|


## Request

### Request URL

#### Recent log file

```
{CellURL}__log/current
```

#### Log file that is rotated

```
{CellURL}__log/archive
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
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Depth|To get the hierarchy of a resource|0:Gets target resource only<br>1:Gets target and resources directly under the target|Yes||

### Request Body

#### Namespace

|URI|Overview|notes()prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

#### Structure of XML

The body is XML and follows the following schema.

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|propfind|D:|Element|Represents the root element of propfind, and allprop is a child.||
|allprop|D:|Element|Represent setting to retrieve all properties|allprop : get all properties<br>Even if the request body is empty, treat it as allprop<br>Elements other than allprop are not supported for v1.2 , v1.1|

#### DTD notation

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
|207|Multi-Status|when acquire succeed|

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|MimeType depending on Resource|"application/xml"|
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Valid version|

### Response Body

#### Namespace

|URI|Overview|Reference Prefix|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|
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
|status|D:|Element|Represents the response code of resource acquisition||
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

#### DTD notation

#### Namespace: D:

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

#### Namespace:p:

```dtd
<!ELEMENT odata EMPTY>
<!ELEMENT service EMPTY>
```

#### Namespace: xml:

```dtd
<!ATTLIST acl base CDATA #IMPLIED>
```

### Response Sample

#### resourcetype element

```xml
<?xml version="1.0" encoding="utf-8"?>
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

In addition, it is planned to specify the file ZIP compaction flag at the time of log file rotation. By default (log configuration update API) is uncompressed.  
In this case, based on the log file compression flag, file name of href component and Mime Type of getcontenttype component will switch.

|ZIP compression flag|File name of href component (ex:)|Value of getcontenttype|Notes|
|:--|:--|:--|:--|
|Uncompressed|default.log.1364460341902|text/csv|Applies the same even at the case of no rotation|
|Compressed|default.log.1364460341902.zip|application/zip||

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

## cURL Command

```sh
curl "https://cell1.unit1.example/__log/archive" -X PROPFIND -i -H 'Depth:1' \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json'
```


