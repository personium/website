---
id: 293_OAuth2_Token_Endpoint
title: OAuth 2.0 Token Endpoint
sidebar_label: OAuth 2.0 Token Endpoint
---

## Overview

An API endpoint that issues access tokens to access various APIs in the cell. It complies with the OAuth 2.0 specification, it authenticates users and applications in various ways and issues tokens such as access / refresh tokens.

### Variation of user authentication

#### Account holder authentication with password

* Resource Owner Password Credential (ROPC) flow in OAuth 2.0.
* Based on the registered account name and password, you can authenticate the owner of the account and receive access token issuance.
* As a defense against brute force attack, even if the password is legitimate for that account for one second after failure of authentication, an authentication error will result.
* This flow should be used only by cell administration applications such as Cell GUI, which cell owners place high levels of trust.
* As described in the OAuth 2.0 specification, general Personium applications should not use this flow.

#### Authentication of other cell user by transcell access token

* The authentication method corresponding to the SAML 2 assertion flow of the OAuth 2.0 extension.
* You can issue an access token by authenticating another cell user by sending a transcell access token addressed to this cell.
* Re-authentication of the application is required here even if application authentication has been undergone when issuing a transcell access token to be transmitted.

#### Continuation of user authentication by refresh token transmission

* By sending a refresh token, it is possible to receive a new access token that inherited the user authentication state received when the refresh token was issued.
* Re-authentication of the application is required here even if application authentication has been undergone when issuing a refresh token to be transmitted.
* Applications cannot be switched at token refresh by sending client_id different from the originally used one when the refresh token is issued.
* Use OpenID Connect ID tokens in cases that authenticated state should be transferred form one app to another, such as single-sign-on from a cell application to a general application.
* Access tokens or refresh tokens should not be shared or exchanged among applications.

### Information transmission for application authentication

* Personium uses OAuth's client authentication framework to authenticate the application.
* Personium uses the schema URI of the application as client_id. In many cases the schema URI is the URL of the applet.
* Personium uses an application authentication token as client_secret.
* Information transmission for application authentication is not mandatory.

### Variation of issue token specification

#### Issuing an access token

If there is no parameter specified as p_target, it will issue a valid access token (cell local access token) in this cell.

#### Issuing a Transcell Access Token

By specifying the URL of another cell by using the parameter called p_target, we issue a Transcell access token for accessing other cells
### Other variations

#### Issuing cookies

* If p_cookie is specified as a true value, cookies that are valid only in this cell are issued.
* This cookie alone does not substitute for the access token, but by using it together with the character string "cookie_peer" issued at the same time, it has the same effect as the access token.
* When you get a resource on this cell, access this URL by adding this value with a query parameter called cookie_peer to the URL so that it handles the same as access token transmission only when correspondence with cookies sent at the same time is obtained.
* With this, it is possible to display private media only to authorized users using tags such as HTML img video audio.
* Cookies that are issued are valid only in this cell and can not be used in combination with p_target, which is a token acquisition parameter for accessing other cells.

### Record of authentication history

In case of password authentication (when "password" is set at the time of request as grant_type), the last authentication date and number of authentication failure are recorded as authentication history.<br>
An account that does not record authentication history can be set in [Target cell property setting](./291_Cell_Change_Property.md).

Target cell property setting  
```xml
<p:accountsnotrecordingauthhistory>{Account name(can specify multiple items separated by commas)}</p:accountsnotrecordingauthhistory>
```

## Request

### Request URL

```
{CellURL}/__token
```

### Request Method

POST

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

|Item Name|Overview|Format|Required|Effective Value|
|:--|:--|:--|:--|:--|
|Authorization|Specifies client authentication information in the Basic authentication format|Basic {String}|No|As defined in OAuth2.0 spec, client authentication can be performed using Basic auth format in this header. Just send base64url Encoded value of the string {{Schema Authenticator's source URL}: {Token paid out from the schema authentication source}} followed by the fixed string "Basic . If request body has client_assertion or client_assertion_type parameters, then they will have the priority. On the other hand, the setting of the authorization header takes precedence over client_id and client_secret in the request body.|
|Content-Type|Specifies the request body format|application/x-www-form-urlencoded|No|[application/x-www-form-urlencoded]by default|

### Request Body

|Item Name|Overview|Format|Required|Effective Value|
|:--|:--|:--|:--|:--|
|grant_type|grant type defined in OAuth 2.0  (RFC6749)|String|Yes|password<br>urn&#58;x-personium:oidc:google<br>urn&#58;ietf:params:oauth:grant-type:saml2-bearer<br>authorization_code<br>refresh_token|
|username|User name|String|Yes(When grant_type = password)|Registered user name|
|password|Password|String|Yes(When grant_type = password)|Registered password|
|assertion|Transcell token target|String|Yes(When grant_type=urn&#58;ietf:params:oauth:grant-type:saml2-bearer)|A valid transacell access token|
|code|Authorization Code|String|Yes(When grant_type = authorization_code)|Valid authorization code|
|refresh_token|Refresh token|String|Yes(When grant_type=refresh_token)|Effective refresh token|
|id_token|Token ID|JSON Web Token|Yes(grant_type=urn&#58;x-personium:oidc:For google)|JWT Formed ID Token|
|p_target|Issue target|String|No|Where to use the token to be paid (cell URL)<br>If specified, it becomes transcellation token authentication|
|client_assertion_type|Type of client_assertion|String|No|Only valid value is "urn:ietf:params:oauth:grant-type:saml2-bearer" defined in RFC7522. When this parameter or client_assertion is specified, then client authentication will be performed in the manner defined in RFC7522, and the content of Authorization header or client_sercret is neglected.|
|client_assertion|Application authentication token|String|No|An application authentication token issued from an application cell, etc. When this parameter and client_assertion_type are specified, then client authentication will be performed in the manner defined in RFC7522, and the content of Authorization header or client_sercret is neglected.|
|client_id|Application schema URI|String|Yes(When grant_type = authorization_code)|In many cases App store URL<br>When specified with client_secret Is issued application-certified token<br>At the same time, if the same information is transmitted in the Authorization header, the setting of the Authorization header takes precedence|
|client_secret|Application authentication token|String|No|An application authentication token issued from an application cell, etc. When specified with client_id, issue an application-certified token. If the same information is transmitted in the Authorization header, the setting of the Authorization header takes precedence.|
|scope|Scope request|String|No|Space-separated scope identifiers that app requests|
|p_owner|ULUUT promotion execution Query|String|No|Valid only for true|
|p_cookie|Authentication cookie issuance option<br>If specified, issue an authentication cookie<br>When p_target is specified, specification of this parameter is ignored|String|No|Valid only for true|
|expires_in|Access token expiration in (sec)|Int<br>1～3600|No|Specify expiration in of issued access token<br>The default is 3600 (1 hour)|
|refresh_token_expires_in|Refresh token expiration in (sec)|Int<br>1～86400|No|Specify expiration in of issued refresh token<br>The default is 86400 (24 hours)<br>When p_owner is specified, specification of this parameter is ignored|

### Request Sample

Password authentication

```
grant_type=password&username=username&password=pass
```

Issuing a transcell access token with account owner authentication by password

```
grant_type=password&username=username&password=pass&p_target=https://cell1.unit1.example/
```

Issuing application-authenticated access token by password owner authentication and application authentication token sending

```
grant_type=password&username=username&password=pass&client_id=https://app-cell1.unit1.example/
&client_secret=WjzDmvJ...(snip)...4nHgo

```

Account holder authentication by Google ID issued Open ID Connect Id Token

```
grant_type=urn:x-personium:oidc:google&id_token=IDTOKEN
```

Refreshing tokens with refresh tokens

```
grant_type=urn:ietf:params:oauth:grant-type:saml2-bearer&assertion=WjzDmvJ...(snip)...4nHgo
```

Cookies are also issued by password owner authentication

```
grant_type=password&username=username&password=pass&p_cookie=true
```

## Response

### Response Code

200

### Response Header

|Item Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|application/json||
|Set-Cookie|Cookie authentication information (p_cookie)|Only when setting cookie issue option (p_cookie) at request|

### Response Body

|Item Name|Overview|Notes|
|:--|:--|:--|
|access_token|Access token||
|refresh_token|Refresh token|*If p_owner is set at the time of request, it will not be returned|
|token_type|Bearer||
|scope|scopes that are granted to the token issued upon the requet|Multiple scopes may be returned using space-separated syntax|
|expires_in|Access token expiration in (sec)|Expiration date set at the time of request<br>The default is 3600 (1 hour)|
|refresh_token_expires_in|Refresh token expiration in (sec)|Expiration date set at the time of request<br>The default is 86400 (24 hours)<br>*If p_owner is set at the time of request, it will not be returned|
|id_token|id_token available with OpenID Connect|Return only if<br>grant_type=authorization_code and<br>scope of code is openid|
|p_cookie_peer|Cookie Authentication Value|Authentication value specified at the time of cookie authentication<br>\*Return only when the cookie issue option (p_cookie) is set at the time of request|
|last_authenticated|Last authentication date and time|Last authentication date and time (UNIX time of long type)<br>initial authentication is null<br>\*Return only when password is set as authorization type (grant_type) at the time of request|
|failed_count|Number of authentication failures|Number of consecutive failures in password authentication since last authentication<br>\*Return only when password is set as authorization type (grant_type) at the time of request|

### Response Sample

```JSON
{
  "access_token": "AA~PBDc...(snip)...FrTjA",
  "refresh_token_expires_in": 86400,
  "refresh_token": "RA~uELM...(snip)...yWMoQ",
  "token_type": "Bearer",
  "scope": "root",
  "expires_in": 3600,
  "last_authenticated": 1486462510467,
  "failed_count": 2
}
```

### Authentication failed
Return an error response. Refer to the "Authentication API" of [Error Message List](004_Error_Messages.md).<br>
The response body is as follows.

|Item Name|Overview|Notes|
|:--|:--|:--|
|error|OAUTH error code||
|error_description|[{Message code}] - {Message}|Returns a string that combines the message code and the message.|
|access_token|Access token|Return only when the message code is "PR401-AN-0001".<br>Return the access token that can only change the password.|
|url|URL|Return only when the message code is "PR401-AN-0001".<br>The URL of the password change API is returned.|
|last_authenticated|Last authentication date and time|Return only when the message code is "PR401-AN-0001"|
|failed_count|Number of authentication failures|Return only when the message code is "PR401-AN-0001"|

## cURL Command

### Account holder authentication

```sh
curl "https://cell1.unit1.example/__token" -X POST -i \
-d 'grant_type=password&username=user1&password=pass'
```

### Other cell user authentication

```sh
curl "https://cell1.unit1.example/__token" -X POST -i \
-d 'grant_type=urn:ietf:params:oauth:grant-type:saml2-bearer&assertion=WjzDmvJ...(snip)...4nHgo'
```

### Token Refresh

```sh
curl "https://cell1.unit1.example/__token" -X POST -i \
-d 'grant_type=refresh_token&refresh_token=RA~uELM...(snip)...yWMoQ'
```

### Account holder + Application authentication

```sh
curl "https://cell1.unit1.example/__token" -X POST -i \
-d 'grant_type=password&username=name1&password=pass&client_id=\
https://app-cell1.unit1.example/&client_secret=WjzDmvJ...(snip)...4nHgo'
```

### Issuing transcell access token for other cell by other cell user authentication
```sh
curl "https://cell1.unit1.example/__token" -X POST -i \
-d 'grant_type=urn:ietf:params:oauth:grant-type:saml2-bearer&assertion=\
WjzDmvJ...(snip)...4nHgo&p_target=https://cell1.unit1.example/'
```
