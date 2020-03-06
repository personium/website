---
id: version-1.7.21-291_Cell_Change_Property
title: Change Properties
sidebar_label: Change Properties
original_id: 291_Cell_Change_Property
---

## Overview

change Cell properties

### Required Privileges

Only unit users permitted

## Request

### Request URL

```
{CellURL}
```

### Request Method

PROPPATCH

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specify content format|application / xml|No||
|Accept|Specify acceptable media types in response|application / xml|No||

### Request Body

|Item Name|Namespace|Overview|Required|Effective Value|Notes|
|:--|:--|:--|:--|:--|:--|
|DAV:||XML namespace setting|Yes|"DAV:"||
|urn: x-personium: xmlns||XML namespace setting|Yes|"Urn: x-personium: xmlns"||
|propertyupdate|DAV:|propertyupdate (Access Control List) root|Yes|<ELEMENT propertyupdate! (Set &#124; remove)>||
|set|DAV:|set property|No|<! ELEMENT set (prop *)>||
|remove|DAV:|remove property|No|<! ELEMENT set (prop *)>||
|prop|DAV:|property value|No|<! ELEMENT prop ANY>|Set or Delete using the XML tag specified as ANY as a key|

\* The following are reserved by the system.
  * p:relayhtmlurl (For details, see [Get Cell Root](./200_Cell_Root.md))
  * p:authorizationhtmlurl (For details, see [OAuth2.0 Authorization Endpoint](./292_OAuth2_Authorization_Endpoint.md))
  * p:authorizationpasswordchangehtmlurl (For details, see [OAuth2.0 Authorization Endpoint](./292_OAuth2_Authorization_Endpoint.md))
  * p:accountsnotrecordingauthhistory (For details, see [OAuth2.0 Token Endpoint](./293_OAuth2_Token_Endpoint.md))

### Request Sample

```xml
<D:propertyupdate xmlns:D="DAV:"
    xmlns:p="urn:x-personium:xmlns">
  <D:set>
    <D:prop>
      <p:foo>bar</p:foo>
    </D:prop>
  </D:set>
  <D:remove>
    <D:prop>
      <p:foo/>
    </D:prop>
  </D:remove>
</D:propertyupdate>
```


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|207|MULTI_STATUS|Success|

### Response Header

None

### Response Body

|Item Name|Namespace|Overview|Notes|
|:--|:--|:--|:--|
|multistatus|DAV:|Response Body route|<! ELEMENT multistatus (response *)>|
|response|DAV:|response route|<! ELEMENT response (href, propstat)>|
|href|DAV:|URL of the resource that executed PROPPATCH|URL of the resource that executed PROPPATCH|
|propstat|DAV:|rproperty setting result|<! ELEMENT propstat (prop, status)>|
|prop|DAV:|property setting contents|display resource setting result as following <br>success: setting key and value<br>delete success: deleted key|
|status|DAV:|Property setting status code|In the case of setting success 200 (OK) is returned|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```xml
<multistatus xmlns="DAV:">
  <response>
    <href>https://cell1.unit1.example/</href>
    <propstat>
      <prop>
        <p:foo xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:">bar</p:foo>
        <p:foo xmlns:p="urn:x-personium:xmlns" xmlns:D="DAV:"/>
      </prop>
      <status>HTTP/1.1 200 OK</status>
    </propstat>
  </response>
</multistatus>
```


## cURL Command

```sh
curl "https://cell1.unit1.example/" -X PROPPATCH -i \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-d '<?xml version="1.0" encoding="utf-8" ?>\
<D:propertyupdate xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns"><D:set><D:prop>\
<p:foo>bar</p:foo></D:prop></D:set><D:remove><D:prop><p:foo/></D:prop>\
</D:remove></D:propertyupdate>'
```
