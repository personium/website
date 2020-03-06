---
id: version-1.7.21-292p_OAuth2_Authorization_Endpoint
title: POST acceptance at OAuth2.0 Authorization Endpoint
sidebar_label: POST acceptance at OAuth2.0 Authorization Endpoint
original_id: 292p_OAuth2_Authorization_Endpoint
---

## Overview
POST Method is accepted at OAuth2 Authorization Endpoint.
It is designed to receive form payload sent from the HTML returned from the successful GET request at the OAuth2 Authorization Endpoint.

### Restrictions
For scope=openid, only the following response_type can be specified.  

* response_type=id_token
* response_type=code

## Request
### Request URL
```
{CellName}/__authz
```

### Request Method

POST

### Request Body
|Item Name|Overview|Format|Required|Effective Value|
|:--|:--|:--|:--|:--|
|response_type|Response Type|String|Yes|token, code, id_token(scope=openid required)|
|client_id|Application Cell URL|String|Yes|Application Cell URL of authentication form request|
|redirect_uri|Client redirect endpoint URL|String|Yes|URL of the redirect script registered under the default BOX of the application cell<br>Query parameters formatted with application/x-www-form-urlencoded can be included<br>It is not possible to include fragments<br>Effective digit length:512byte|
|state|Random value used to maintain state between request and callback|String|No|Random value<br>Effective digit length:512byte|
|scope|Access scope requested|String|No|Personium can specify "openid"|
|username|User name|String|No|Registered user name<br>\* When  Authentication form request, specification of this parameter is ignored|
|password|Password|String|No|Registered password<br>\* When  Authentication form request, specification of this parameter is ignored|
|expires_in|Access token expiration in (sec)|Int<br>1～3600|No|Specify expiration in of issued access token<br>The default is 3600 (1 hour)<br>* When response_type is other than token, specification of this parameter is ignored|
|cancel_flg|Canceled flag|Boolean|No|User cancellation flag for authorization process<br>If true is set, it shall be canceled by the user|
|password_change_required|Password change required flag|Boolean|No|A flag indicating whether the authenticated account required password change<br>* Password_change_required returned in response to authorization request|
|access_token|Access token|String|No|Specify Access Token for Authenticated Account<br>* access_token returned in response to authorization request|

### Request Header
None

### Request Query
None

## Response (Authorization processing request)
Perform authorization processing. The redirect destination and URL parameters differ depending on the processing result.  
The pattern of the processing result is as follows.
- Authorization processing success (Implicit grant)
- Authorization processing success (Grant Code)
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

### Authorization processing success (Grant Code)
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

### Authorization processing success (ID Token issuance)
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


## cURL Command

```sh
curl "https://cell1.unit1.example/__authz" -X POST -i \
-d 'response_type=token&client_id=https://app-cell1.unit1.example/&\
redirect_uri=https://app-cell1.unit1.example/__/redirect.md&\
state=0000000111&username=account1&password=pass'
```
