---
id: 003_Auth
title: Authorization Model
sidebar_label: Authorization model
---

## Introduction

This section describes the authorization model that is important when using Personium. The following three key concepts are the basics of Personium's authorization model.

1. Cell-centric authorization
1. RBAC (Role Based Access Control)
1. App authorization


-------------------------------------------------------------------------------

## Cell-centric authorization

### Assuming data access

To explain cell-centric authorization, assume a situation in which personal data is accessed. The following figure shows a comparison of data access before and after PDS.

![before-after](assets/auth/before-after.png)

The following roles appear when accessing data with PDS.

| Role name | Description |
|-------|----|
| Data subject | Data owner. In the above figure, it indicates Alice, Bob, Carol. |
| Data Accessor | Person who accesses data. This includes cases where not only the data subject but also those other than the data subject. |
| Apps | Applications that data accessors use to access data on their behalf. |
|Authorization server |A server that authorizes data access. |
|PDS| A server that stores data in units of data. |

As shown in the figure above, the data accessor normally accesses the PDS through the application, and the access is controlled by the authorization server in the PDS.

Personium adopts an authorization model centered on data subjects (mainly individuals) as shown on the right, instead of the service-centered authorization model shown on the left.

Therefore, in Personium, the data subject is expressed in units of cells, each cell has an independent URL, and has an authorization mechanism. Specifically, each cell holds two endpoints (Authz and Token) of OAuth2, which is the authorization framework. The following table shows examples of specific URLs for each data subject.

|Data Subject|Cell URL|OAuth2 Authorization Endpoint|OAuth2 Token Endpoint|
|----|----|----|----|
|Alice|https://alice.example/|https://alice.example/__authz|https://alice.example/__token|
|Bob|https://bob.example/|https://bob.example/__authz|https://bob.example/__token|
|Carol|https://carol.example/|https://carol.example/__authz|https://carol.example/__token|

When accessing data, authorization is performed using these endpoints and it is controlled so that only appropriate data accessors can access.

### Data access to own cell

When thinking about data access, first consider the case of simply accessing the cell directly without going through the application.

When Alice, the data subject, accesses her own data in the cell, she does it in the following order.

1. Authenticate to the token endpoint of the Alice cell and obtain an access token
2. Access data in Alice cell with access token

![Access owner's data](assets/auth/access_owner_data.png)

When performing authentication at the token endpoint, use the Account (for example, me) that represents the data subject created in advance and the password. [^1] Also, at this time, the data is accessed by the Role linked to the preset Account.

Roles are used for data access control and are described in detail in the RBAC section.

The access scope of the access token obtained by this method is within Alice's own cell.

[^1]: Authentication service outside Personium is also available. We plan to support authentication methods other than passwords in the future.

### Data access to other cell

Next, consider data access to another cell where Alice accesses Bob's data. Please perform the following in advance:

- Add Alice cell to Bob cell's ExtCell and link Alice's Role as seen by Bob

Follow the steps below to access the data.

1. Set the issue target parameter (p_target) to Bob cell for the token endpoint of Alice cell, authenticate and obtain the trans cell token
2. Access data in Bob cell with transcell token

![Access other owner's data](assets/auth/access_other_data.png)

Personium controls data access based on the trust relationship between cells. By setting Alice cell as Bob's ExtCell and linking the Role, Bob's data is accessed by Alice using that Role. In the above figure, the ExtCell (Alice) and Role called Secretary are linked, so Bob's data is accessed as Secretary.

The access scope of the transcell token obtained by this method is within Bob's cell.

### Accessing other cell's data by token exchange

Other cell's data can also be accessed by the token exchange method.

The transcell token described above is verified according to SAML2 Assertion, so the token is long. Therefore, performance tends to deteriorate due to client-server communication and server-side verification processing. Performance can be improved by exchanging a shorter tokens.

The token exchange method has similar procedure for obtaining transcell tokens, only with an additional step.

Please perform the following in advance.

-Add Alice cell to Bob cell's ExtCell and link Alice's Role as seen by Bob

Token exchange will be performed in the following order.

1. Set the issue target parameter (p_target) to Bob cell for the token endpoint of Alice cell, authenticate, and obtain the trans cell token
2. Authenticate with the transcell token against the token endpoint of Bob cell, and obtain the access token from Bob cell
3. Access data in Bob cell with access token

![Access other owner's data by token exchange](assets/auth/access_other_data_by_exchange.png)

The access Role and access scope are the same as the transcell token.

### token renewal

When you get the access token or transcell token, a refresh token is issued for renewing the token's expiration date.

To renew the access token using the refresh token, perform the following procedures.

1. Authenticate to the token endpoint of Alice cell, get access token and refresh token
2. Send the grant_type=refresh_token parameter and refresh token to the token endpoint in the Alice cell

![Refresh Access token](assets/auth/refresh.png)

### Administrative token

So far, the data access method described assumes that an existing cell with data and an account to access the cell are available. However, no cell exist immediately after building the Personium unit. It is necessary to create it. In addition, an operator who is not the data subject must operate on the cell.

`Unit master token` and `unit user token` are prepared as administrative tokens for performing the above operations.

Please refer to [Unit User](../unit-administrator/Unit-User) for details.

### Token type

Many tokens have been introduced to access data and they are summarized in the table below.

| Token type | Description | Expiration date |
|----|----|----|
| Cell Local Token | Access token valid in the cell that issued the token | 1 hour |
| Trans-cell token | Access token valid in the target cell specified by the issued cell | 1 hour |
| Refresh Token | Token used to refresh an already issued token | 24 hours |
|Unit Master Token |Administrative token used for initial settings such as cell creation immediately after unit construction, development and testing |-|
| Unit user token | Administrative token used for operations such as cell creation |-|

-------------------------------------------------------------------------------

## RBAC (Role Based Access Control)

In the previous section, it was stated that Role is determined by Account in the authenticated cell and the relationship between cells. Personium has a mechanism of RBAC (Role Based Access Control) that controls how much data access is allowed by this Role.

A user controls access by setting which Role can perform what operation (ACL) for each resource.

![ACL](assets/auth/acl-role.png)

Please refer to [Access Control Model](../apiref/006_Access_Control.md) for details.

-------------------------------------------------------------------------------

## App authorization

So far, for simplicity we have described a data access method that does not pass through the application. However, when the data accessor actually accesses the data, it basically does not directly access the cell and transfers the data access to the application.

Also, in order to utilize the data on PDS, it is necessary to have abundant applications.

-App that provides data
-App that uses data

To do so, it is necessary to utilize open APIs that allow not only one business operator to develop and provide applications but also other business operators. This section describes the outline of application authorization under such assumptions.

### OAuth in PDS

Appropriate delegation of authority is required to allow apps that take various forms of provision to access data securely.
Personium uses OAuth, which is a framework for app authorization and delegation, to achieve these.

As described above, Personium has the function of the authorization server in each cell. If you apply to OAuth characters in this case, it will be as shown in the following figure.

![OAuth in PDS](assets/auth/pds_oauth.png)

The specific authorization flow differs depending on the grant_type, and Personium supports the following grant_type.

- ROPC (Resource Owner Password Credential)
- Authorization code
- Implicit

grant_type is selected according to the form of the application (whether it is a trusted application, server side web application or native application, etc.). We recommend the following as selection criteria:

|grant_type|Selection Criteria|
|----------|-------|
|ROPC|Adopted when the app and the app provider are highly reliable, such as when the operator and the app provider are the same. |
|Authorization code | Adopted when the PDS provider and the application provider are different. For native apps, we recommend using PKCE together, which will be added in the future. |
| Implicit | Basic deprecation. |

Next, the ROPC and authorization code flow will be explained.

### ROPC (Resource Owner Password Credential) flow

![ROPC Flow](assets/auth/ROPC.png)

This is a simple flow of providing username/password to the application and receiving an access token.

This flow can be used when the reliability of the application is high. Such as when the PDS provider and the application provider are the same. If not, use the authorization code flow explained below.

### Authorization code flow

In the authorization code flow, after entering the data access agreement/username/password on the screen on the PDS, the application receives the short-lived authorization code once, and sends the authorization code from the application to the PDS to obtain the access token.

![Authorization Code Flow](assets/auth/personium-authz-code-flow/personium-authz-code-flow.png)

Details are described in the section [App authentication](../app-developer/app_authn.md).

### Box protection

in preparation
