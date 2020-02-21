---
id: version-1.7.18-289_Cell_ACL
title: Cell Level Access Control Configuration
sidebar_label: Cell Level Access Control Configuration
original_id: 289_Cell_ACL
---

## Overview

Provides cell level access control functions.

### Required Privileges

acl

### Restrictions

Updating the ACL configuration overwrites existing ACL settings.

* Restrictions in V 1.0
    * The function to deny ACL configuration (deny)
    * Acquisition of a list of privileges configurable by the ACL


## Request

### Request URL

```
{CellURL}
```

### Request Method

ACL

### Request Query

Common Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Common Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|PCS-${32 character string with UUID} by default|

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|

### Request Body

### Namespace

|URI|Overview|Notes (prefix)|
|:--|:--|:--|
|DAV:|WebDAV Namespace|D:|
|urn&#58;x-personium:xmlns|Personium namespace|p:|

\* Reference The prefixes are for making it easier to read the following table, but the use of these prefix strings is not ensured or requested.

### Structure of XML

The body is XML and follows the following schema.  
For details on the privilege settings within the privilege tag, please refer to the acl\_model ([Access Control Model](006_Access_Control.md)).

|Node name|Namespace|Node type|Overview|Notes|
|:--|:--|:--|:--|:--|
|acl|D:|Element|Denotes the root of the ACL (Access Control List); one or more ace nodes will be its child||
|base|D:|Element|Denotes the basis of the URL described in the href tag, and takes any value as the attribute value.||
|ace|D:|Element|Denotes an ACE (Access Control Element); a pair of principal and grant will be its child; * When property is acquired, "inherited" is added to the inherited ACE child|"invert", "deny", and "protected" are not supported|
|principal|D:|Element|Denotes the privilege configuration target; href or all will be its child||
|grant|D:|Element|Denotes the privilege grant setting; one or more privilege nodes will be its child node||
|href|D:|Element|Denotes the privilege configuration target role and is the text node to input the role resource URL|Specify the resource URL of the privilege configuration target role<br>It is possible to shorten the URL using the xml:base attribute setting in the acl element|
|all|D:|Element|All access entity privilege setting|The setting for all roles and non-authorized access entities (without the Authorization header)|
|inherited|D:|Element|Denotes the authority inheritance source, href (URL of the authority inheritance source collection) is a child|* Configuration disabled (This element is given only when acquiring properties, and ignored when setting ACL)|
|privilege|D:|Element|Denotes the privilege setting; one of the following elements will be its child||
|root|p:|Element|All privileges||
|auth|p:|Element|Authentication management API editing and viewing privileges||
|auth-read|p:|Element|Authentication management API viewing privileges||
|message|p:|Element|Message management API editing and viewing privileges||
|message-read|p:|Element|Message management API viewing privileges||
|event|p:|Element|Event management API editing and view privileges||
|event-read|p:|Element|Event management API viewing privileges||
|log|p:|Element|Event bus log API editing and viewing privileges||
|log-read|p:|Element|Event bus log API viewing privileges||
|social|p:|Element|Relation management API editing and viewing privileges||
|social-read|p:|Element|Relation management API viewing privileges||
|box|p:|Element|Box management API editing and viewing privileges||
|box-read|p:|Element|Box management API viewing privileges||
|box-install|p:|Element|Box installation execution privileges * supported by V 1.2.3||
|box-export|p:|Element|Box export execution privileges|Unsupported (Configuration disabled)|
|acl|p:|Element|ACL management API editing and viewing privileges||
|acl-read|p:|Element|ACL management API viewing privileges||
|propfind|p:|Element|Property acquisition API viewing privileges||
|rule|p:|Element|Event Processing Rule management API editing and viewing privileges||
|rule-read|p:|Element|Event Processing Rule management API viewing privileges||

#### DTD notation

Namespace: D:

```dtd
<!ELEMENT acl (ace*) >
<!ATTLIST acl base CDATA #IMPLIED>
<!ELEMENT ace ((principal or invert), (grant or deny), protected?,inherited?)>
<!ELEMENT principal (href or all)>
<!ELEMENT principal (privilege+)>
<!ELEMENT href (#PCDATA)>
<!ELEMENT all EMPTY>
<!ELEMENT privilege (root or auth or auth-read or message or message-read or event or event-read or 
social or social-read or box or box-read or acl or acl-read or propfind or rule or rule-read)>
```

Namespace:xml:

```dtd
<!ATTLIST acl base CDATA #IMPLIED>
```

Namespace: p:

```dtd
<!ELEMENT root EMPTY>
<!ELEMENT auth EMPTY>
<!ELEMENT auth-read EMPTY>
<!ELEMENT message EMPTY>
<!ELEMENT message-read EMPTY>
<!ELEMENT event EMPTY>
<!ELEMENT event-read EMPTY>
<!ELEMENT log EMPTY>
<!ELEMENT log-read EMPTY>
<!ELEMENT social EMPTY>
<!ELEMENT social-read EMPTY>
<!ELEMENT box EMPTY>
<!ELEMENT box-read EMPTY>
<!ELEMENT box-install EMPTY>
<!ELEMENT box-export EMPTY>
<!ELEMENT acl EMPTY>
<!ELEMENT acl-read EMPTY>
<!ELEMENT propfind EMPTY>
<!ELEMENT rule EMPTY>
<!ELEMENT rule-read EMPTY>
```

### Request Sample

```xml
<?xml version="1.0" encoding="utf-8" ?>
<D:acl xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns" xml:base="https://example.com/testcell1/__role/box1/">
  <D:ace>
    <D:principal>
      <D:all/>
    </D:principal>
    <D:grant>
           <D:privilege><p:auth/></D:privilege>
           <D:privilege><p:box/></D:privilege>
    </D:grant>
  </D:ace>
  <D:ace>
    <D:principal>
      <D:href>role</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><p:root/></D:privilege>
    </D:grant>
  </D:ace>
</D:acl>
```


## Response

### Response Code

|Code|Message|Overview|
|:--|:--|:--|
|200|OK|Success|

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|Format of data to be returned||

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

## cURL Command

```sh
curl "https://cell1.unit1.example/" -X ACL -i -H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' \
-H 'Accept: application/json' -d '<?xml version="1.0" encoding="utf-8" ?><D:acl xmlns:D="DAV:" \
xmlns:p="urn:x-personium:xmlns" xml:base="https://cell1.unit1.example/__role/box1/">  \
<D:ace><D:principal><D:href>role1</D:href></D:principal><D:grant><D:privilege><p:box-read/>\
</D:privilege><D:privilege><p:auth/></D:privilege></D:grant></D:ace></D:acl>'
```

