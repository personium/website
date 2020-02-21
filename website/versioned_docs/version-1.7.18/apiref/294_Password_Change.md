---
id: version-1.7.18-294_Password_Change
title: Change Password(\_\_mypassword)
sidebar_label: Change Password(\_\_mypassword)
original_id: 294_Password_Change
---

## Overview

An API that performs operations on the account's password

### Change password of own account

Change password of your account.  
\* The Account update API can also change the password of the Account, but this requires the auth authority of the cell level ACL and uses it for management purposes.  
\* Because of changes to the account, CellLocalToken by account authentication is mandatory, not UnitUserToken.  
\* If the account status is "passwordChangeRequired", it will be updated to "active".

### Required Privileges

None


## Request

### Request URL

```
{CellName}/__mypassword
```

### Request Method

PUT

### Request Query

None

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {CellLocalToken}|Yes|The authentication token is a cell local token acquired by the authentication token acquisition API|
|X-Personium-Credential|Password after change|String|Yes|\* Follow the password restrictions of unit setting<br>The default is as follows<br>Number of character:6 - 32<br>Character type: Half size alphanumeric characters and following half-width symbol<br>-_!$\*=^\`{&#124;}~.@|

### Request Body

None


## Response

### Response Code

204

### Response Header

None

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)


## cURL Command

```sh
curl "https://cell1.unit1.example/__mypassword" -X PUT -i -H \
'X-Personium-Credential: change_password' -H 'Authorization: Bearer AA~4l...(snip)........auMhw' -H \
'Accept: application/json'
```
