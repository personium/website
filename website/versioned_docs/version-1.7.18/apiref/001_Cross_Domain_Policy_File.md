---
id: version-1.7.18-001_Cross_Domain_Policy_File
title: Retrieve Cross-Domain Policy File
sidebar_label: Retrieve Cross-Domain Policy File
original_id: 001_Cross_Domain_Policy_File
---

## Overview

Gets the (crossdomain.xml) cross-domain policy file.  
You can get the Cross-domain policy file of all users.

## Request

### Request URL

```
/crossdomain.xml
```

### Request Method

GET

### Request Query

None

### Request Header

None

### Request Body

None


## Response

### Response Code

200

### Response Header

None

### Response Body

XML

|Item Name|Overview|
|:--|:--|
|/cross-domain-policy/site-control|Permission settings of meta-information policy. Return the "permitted-cross-domain-policies =" all "" attribute value is fixed|
|/cross-domain-policy/allow-access-from|Domain can be accessed in the current domain. Return the "domain =" * "" attribute value is fixed|
|/cross-domain-policy/allow-http-request-headers-from|And header information that can be sent, the source domain to the domain of the current header. Return the "domain =" * "headers =" * "" attribute value is fixed|

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

## cURL Command

```sh
curl "https://unit1.example/crossdomain.xml" -X GET -i
```


