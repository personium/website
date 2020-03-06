---
id: version-1.7.21-292_OAuth2_Authorization_Endpoint
title: OAuth 2.0 Authorization Endpoint
sidebar_label: OAuth 2.0 Authorization Endpoint
original_id: 292_OAuth2_Authorization_Endpoint
---

## Overview
OAuth 2.0 Authorization Endpoint of a Cell. Usually it returns an HTML to render on Web Browsers, however depending on the state of Cookies and so on, it may directly redirect to the specified URL with grant code, access token or id token.

### Restrictions
For issuing ID tokens of OpenID Connect, only the following combination of parameters setting is supported.

* scope=openid
* response_type=id_token or code

## Request
### Request URL
```
{CellURL}/__authz
```

### Request Method
GET

### Request Query
|Item Name|Overview|Format|Required|Effective Value|
|:--|:--|:--|:--|:--|
|response_type|Response Type|String|Yes|token, code, id_token(scope=openid required)|
|client_id|Application Cell URL|String|Yes|Application Cell URL of authentication form request|
|redirect_uri|Client redirect endpoint URL|String|Yes|URL of the redirect script registered under the default BOX of the application cell<br>Query parameters formatted with application/x-www-form-urlencoded can be included<br>It is not possible to include fragments<br>Effective digit length:512byte|
|state|Random value used to maintain state between request and callback|String|No|Random value<br>Effective digit length:512byte|
|scope|Access scope requested|String|No|Personium can specify "openid"|
|expires_in|Access token expiration in (sec)|Int<br>1～3600|No|Specify expiration in of issued access token<br>The default is 3600 (1 hour)<br>* When response_type is other than token, specification of this parameter is ignored|

### Request Header
None

## Response
Returns HTML to display the authentication form or password change form.  Depending on conditions such as cookie status, or in the case that the request parameter is invalid, however, it may redirect to the redirect endpoint without displaying the form.

### HTML Response
Returns HTML for displaying the authentication form or the password change form that are configured on the cell or the unit.  If nothing is configured default HTML will be returned.  

#### How to configure HTML
HTML can be configured with [Unit setting](../server-operator/unit_config_list.md) or [Target cell property setting](./291_Cell_Change_Property.md). When both configurations exist, the cell configuration will have the priority.  

Unit setting  
```
io.personium.core.cell.authorizationhtmlurl.default={URL of html}
io.personium.core.cell.authorizationpasswordchangehtmlurl.default={URL of html}
```

Target cell property setting  
```xml
<p:authorizationhtmlurl>{URL of html}</p:authorizationhtmlurl>
<p:authorizationpasswordchangehtmlurl>{URL of html}</p:authorizationpasswordchangehtmlurl>
```
The schemes that can be specified as URL are "http", "https", "personium-localunit", "personium-localcell".

#### HTML requirement

This endpoint also accepts POST method to receive the form request payload sent from the configured HTML. Please refer to [this document](./292p_OAuth2_Authorization_Endpoint.md) when implementing the HTML.

### Authentication form display, Password change form display
#### Response Code
200  
#### Response Header
|Header Name|Overview|Notes|
|:--|:--|:--|
|Content-Type|text/html; charset=UTF-8||

#### Response Body
Return authentication form or password change form (HTML).  
If password_change_required set at request is true, password change form will be returned.  
Otherwise, the authentication form is returned.


### Parameter check error (client_id, redirect_uri)
In the case of "client_id, redirect_uri not set" "client_id, Redirect_uri is not in URL format" "cell in client_id and redirect_uri is different"

#### Response Code
303  
The browser is redirected to the system's error page.
```
{error_page_uri}?code={code}
```

#### URL parameter
|Item Name|Overview|Notes|
|:--|:--|:--|
|error_page_uri|Redirect URL|The system's error page "cell URL + __html/error"|
|code|[Personium message code](004_Error_Messages.md)||

### Parameter check error (Other than those above)
In the case of request parameters other than client_id, redirect_uri, username and password, the required items are not set or the setting values ​​are incorrect<br>
Or, if cancel_flg is set to true (cancelled by the user)
#### Response Code
303  
The browser is reducted to the client redirect endpoint URL (the value of "redirect_uri" of the request).  
The fragment or query indicated by "URL parameter" is stored in redirect_uri.  
(If response_type = code, a query is stored; otherwise, a fragment is stored)
```
{redirect_uri}?error={error}&error_description={error_description}&state={state}&code={code}
{redirect_uri}#error={error}&error_description={error_description}&state={state}&code={code}
```
#### URL parameter
|Item Name|Overview|Notes|
|:--|:--|:--|
|redirect_uri|Redirect URL|The URL of the client's redirect split<br>specified by the "redirect_uri" of the request|
|error|Code indicating error content|See "error"|
|error_description|Additional information on errors|Set exception message etc|
|error_uri|Web page URI of additional information on error|Return empty string<br>* Set for future enhancemen|
|state|Value of state set at the time of request||
|code|[Personium message code](004_Error_Messages.md)||

##### error
|Code value|Overview|Notes|
|:--|:--|:--|
|invalid_request|A required parameter is not specified in the request<br>Invalid request parameter format||
|unauthorized_client|Cancel button pressed by user||
|unsupported_response_type|Invalid value of response_type||
|server_error|Server Error||

## Response (After User Authorization)
Perform authorization processing. The redirect destination and URL parameters differ depending on the processing result.  
The pattern of the processing result is as follows.
- Authorization processing success (Implicit grant)
- Authorization processing success (Grant code)
- Authorization processing success (ID Token issuance)
- Authentication failure
- Parameter check error (client_id, redirect_uri)
- Parameter check error (Other than those above)

### Authorization processing success (Implicit grant)
When authorization process is successful and token is specified for response_type of request

#### Response Code
303  
The browser is reducted to the client redirect endpoint URL (the value of "redirect_uri" of the request).  
A fragment indicated by "URL parameter" is stored in redirect\_uri.
```
{redirect_uri}#access_token={access_token}&token_type=Bearer&expires_in={expires_in}&state={state}&last_authenticated={last_authenticated}
&failed_count={failed_count}
* In fact, it will be returned in one line without breaking
```

#### URL parameter
|Item Name|Overview|Notes|
|:--|:--|:--|
|redirect_uri|Client redirect endpoint URL|The value of "redirect_uri" in the request|
|access_token|Access token acquired|Return cell local token or transcell token|
|token_type|Bearer||
|expires_in|Access token expiration in (sec)|Expiration date set at the time of request<br>The default is 3600 (1 hour)|
|state|Value of state set at the time of request|Random value used to maintain state between request and callback|
|last_authenticated|Last authentication date and time|Last authentication date and time（UNIX time of long type）<br>initial authentication is null<br>\*Return only when password authentication|
|failed_count|Number of authentication failures|Number of consecutive failures in password authentication since last authentication<br>\*Return only when password authentication|
|box_not_installed|Box not installed flag|Return true only when Box having appcell URL in schema is not created|

### Authorization processing success (Grant code)
When authorization process is successful and code is specified for response_type of request

#### Response Code
303  
The browser is reducted to the client redirect endpoint URL (the value of "redirect_uri" of the request).  
A query indicated by "URL parameter" is stored in redirect\_uri.

```
{redirect_uri}?code={code}&state={state}&last_authenticated={last_authenticated}&failed_count={failed_count}
```

#### URL parameter
|Item Name|Overview|Notes|
|:--|:--|:--|
|redirect_uri|Client redirect endpoint URL|The value of "redirect_uri" in the request|
|code|Code acquired|Code that can be authorized with "grant_type: authorization_code"|
|state|Value of state set at the time of request|Random value used to maintain state between request and callback|
|last_authenticated|Last authentication date and time|Last authentication date and time（UNIX time of long type）<br>initial authentication is null<br>\*Return only when password authentication|
|failed_count|Number of authentication failures|Number of consecutive failures in password authentication since last authentication<br>\*Return only when password authentication|
|box_not_installed|Box not installed flag|Return true only when Box having appcell URL in schema is not created|

### Authorization processing success (ID Token Issuance)
When authorization process is successful and id_token is specified for response_type of request

#### Response Code
303  
The browser is reducted to the client redirect endpoint URL (the value of "redirect_uri" of the request).  
A fragment indicated by "URL parameter" is stored in redirect\_uri.
```
{redirect_uri}#id_token={id_token}&state={state}&last_authenticated={last_authenticated}&failed_count={failed_count}
```

#### URL parameter
|Item Name|Overview|Notes|
|:--|:--|:--|
|redirect_uri|Client redirect endpoint URL|The value of "redirect_uri" in the request|
|id_token|ID Token acquired|id_token available with OpenID Connect|
|state|Value of state set at the time of request|Random value used to maintain state between request and callback|
|last_authenticated|Last authentication date and time|Last authentication date and time（UNIX time of long type）<br>initial authentication is null<br>\*Return only when password authentication|
|failed_count|Number of authentication failures|Number of consecutive failures in password authentication since last authentication<br>\*Return only when password authentication|
|box_not_installed|Box not installed flag|Return true only when Box having appcell URL in schema is not created|

### Authentication failure
When authentication fails (Password mismatch, account locked, etc.)

#### Response Code
303  
The browser is redacted again to the authorization endpoint (cell URL + \_\_authz).
A query indicated by "URL parameter" is stored in authorization endpoint.
```
{authorization_endpoint_url}?response_type={response_type}&redirect_uri={redirect_uri}&client_id={client_id}&state={state}&scope={scope}
&expires_in={expires_in}&error={error}&error_description={error_description}&error_uri={error_uri}&code={code}
&password_change_required={password_change_required}&access_token={access_token}
* In fact, it will be returned in one line without breaking
```
#### URL parameter
|Item Name|Overview|Notes|
|:--|:--|:--|
|authorization_endpoint_url|authorization endpoint URL(cell URL + \_\_authz)||
|response_type|Value of response_type set at the time of request||
|client_id|Value of client_id set at the time of request||
|redirect_uri|Value of redirect_uri set at the time of request||
|state|Value of state set at the time of request||
|scope|Value of scope set at the time of request||
|expires_in|Value of expires_in set at the time of request||
|error|Code indicating error content|See "error"|
|error_description|Additional information on errors|Set exception message etc|
|error_uri|Web page URI of additional information on error|Return empty string<br>* Set for future enhancemen|
|code|[Personium message code](004_Error_Messages.md)||
|password_change_required|Flag indicating whether the authenticated account is required to change password|Return true only if authentication is possible but password change is mandatory|
|access_token|Access token for authenticated account|Only when password_change_required is true, the access token that can only change the password is returned|

##### error
|Code value|Overview|Notes|
|:--|:--|:--|
|invalid_request|Parameters required for authentication (username, password) are not specified||
|invalid_grant|Authentication failure<br>Account locked||
|unauthorized_client|The client is not authorized<br>Password change is required||
|server_error|Server Error||

### Parameter check error (client_id, redirect_uri)
In the case of "client_id, redirect_uri not set" "client_id, Redirect_uri is not in URL format" "cell in client_id and redirect_uri is different"  
It is the same as "Parameter check error (client_id, redirect_uri)" of "response (authentication form request)".

### Parameter check error (Other than those above)
In the case of request parameters other than client_id, redirect_uri, username and password, the required items are not set or the setting values ​​are incorrect  
Or, if cancel_flg is set to true (cancelled by the user)  
It is the same as "Parameter check error (Other than those above)" of "response (authentication form request)".

## cURL Command

```sh
curl "https://cell1.unit1.example/__authz?response_type=token&\
redirect_uri=https://app-cell1.unit1.example/__/redirect.md&\
client_id=https://app-cell1.unit1.example\
state=0000000111" -X GET -i
```
