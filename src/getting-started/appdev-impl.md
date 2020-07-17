---
id: appdev-impl
title: App implementation
sidebar_label: App implementation
---

We will explain the main API of Personium through the implementation of the sample app created from the template app. The code for the sample app is below.

[app-personium-trails](https://github.com/personium/app-personium-trails)

The dummy Cell URLs used in this sample app are listed below.

|Cell type|URL|
|-------|---|
|Data Subject Cell|https://alice.example/|
|App Cell|https://app-personium-trails.example/|

> Simplified relevant information of the HTTP communications are described for easy understanding.

----

## OAuth 2.0 authorization code flow

If you want to use OAuth 2.0 authorization code flow with Personium, use the following engine script [^1] and Personium API.

* Engine script
  * [app](https://github.com/personium/app-personium-trails/blob/master/src/app/engine/front/launchSPA.js)
  * [start_oauth2](https://github.com/personium/app-personium-trails/blob/master/src/app/engine/auth/start_oauth2.js)
  * [recieve_redirect](https://github.com/personium/app-personium-trails/blob/master/src/app/engine/auth/receive_redirect.js)
* Personium Cell Level API
  * [OAuth 2.0 authorization endpoint](../apiref/292_OAuth2_Authorization_Endpoint.md)
  * [POST acceptance in OAuth2.0 authorization endpoint](../apiref/292p_OAuth2_Authorization_Endpoint.md)
  * [OAuth 2.0 token endpoint](../apiref/293_OAuth2_Token_Endpoint.md)

Detailed sequence diagram available [here](../user_guide/003_Auth.md#authorization-code-flow).

In order to start the sample app, access the engine script endpoint (`https://app-personium-trails.example/__/front/app`) from the web browser. Then, the following screen will prompt you to enter the data subject Cell URL.

![Data Subject Cell URL](assets/getting-started/cell_url_input.png)

Enter the data subject Cell URL `https://alice.example/` to start the asynchronous communication that executes the engine script endpoint (start_oauth2).

```text
# request
POST https://app-personium-trails.example/__/auth/start_oauth2

cellUrl=https://alice.example/

# Response
Status Code: 303
Location: https://alice.example/__authz
?response_type=code
&client_id=https://app-personium-trails.example/
&redirect_uri=https://app-personium-trails.example/__/front/app?cellUrl=https://alice.example/
&state=15933********-per
```

On the server side, this endpoint generates the state parameter used for CSRF (Cross-Site Request Forgery) prevention and then redirects the request to the authorization endpoint. In the parameter redirect_uri, the URL of the application that receives the authorization code is specified. In the sample app, the engine script endpoint (`https://app-personium-trails.example/__/front/app`) is specified.

The HTTP communication to [OAuth 2.0 authorization endpoint](../apiref/292_OAuth2_Authorization_Endpoint.md) is as shown below.

```text
# request
GET https://alice.example/__authz

response_type=code
client_id=https://app-personium-trails.example/
redirect_uri=https://app-personium-trails.example/__/front/app?cellUrl=https://alice.example/
state=15933********-per

# Response
Status Code: 200
Content-Type: text/html;charset=UTF-8

<HTML of authentication form>
```

The above response is rendered as an authentication form.

![Authentication Form](assets/getting-started/oauth_form.png)

Enter UserID and Password and click the login button. The following HTTP communication to [Accept POST at OAuth2.0 authorization endpoint](../apiref/292p_OAuth2_Authorization_Endpoint.md) is performed.

```text
# request
POST https://alice.example/__authz

response_type=code
client_id=https://app-personium-trails.example/
redirect_uri=https://app-personium-trails.example/__/auth/receive_redirect?cellUrl=https://alice.example/
state=15933********-per
username=me
password=mypassword

# Response
Status Code: 303
Location: https://app-personium-trails.example/__/front/app
?cellUrl=https://alice.example/
&last_authenticated=1592968464695
&code=GC~EPET********-9ws
&failed_count=0
&state=15933********-per
```

The authorization code (code) and state parameters are included and further redirected to the engine script endpoint (`https://app-personium-trails.example/__/front/app`) that launches the sample app with necessary information.

```text
# request
GET https://app-personium-trails.example/__/front/app
?cellUrl=https://alice.example/
&last_authenticated=1592968464695
&code=GC~EPET********-9ws
&failed_count=0
&state=15933********-per

# Response
Status Code: 200
Content-Type: text/html;charset=UTF-8

<HTML of sample application>
```

HTTP communication is performed after adding code (authorization code) and state to receive_redirect of engine script by asynchronous communication by Fetch from HTML of sample application.

```text
# request
POST https://app-personium-trails.example/__/auth/receive_redirect

cellUrl=https://alice.example/
code=GC~EPET********-9ws
failed_count=0
state=15933********-per
```

After verifying the state with the process on receive_redirect of the engine script, access [OAuth 2.0 token endpoint](../apiref/293_OAuth2_Token_Endpoint.md) of Personium. HTTP communication is performed as follows.

```text
# request
POST https://alice.example/__token

grant_type=authorization_code
code=GC~EPET********-9ws
client_id=https://app-personium-trails.example/
client_secret=<trans cell token to the data subject Cell authenticated on the application Cell>

# Response
{
  "access_token": "AR~omWD********IPo",
  "refresh_token_expires_in": 86400,
  "refresh_token": "RR~KR9********hbs",
  "p_target": "https://alice.example/",
  "scope": "root",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

The response of the token endpoint is returned as it is as the response of receive_redirect. After that, API operations that require authorization are executed by giving the value of `access_token` obtained here as HTTP header `Authorization: Bearer <access_token>`.

----

## Box installation

If the authorization is successful, the Box installation screen will be displayed.

![Box installation](assets/getting-started/box_install.png)

Click the "Start Install" button to execute the [Box Installation](../apiref/302_Box_Installation.md) API.

```text
# request
MKCOL https://alice.example/app-personium-trails

(bar file of app-personium-trails)

# Response
Status Code: 202
```

Check the progress of Box installation by accessing [Get Box Metadata](../apiref/303_Progress_of_Bar_File_Installation.md) API.

```text
# request
GET https://alice.example/app-personium-trails

# Response
Status Code: 200

{
  "cell": {
    "name": "alice",
    "url": "https://alice.example/"
  },
  "box": {
    "schema": "https://app-personium-trails.example/",
    "name": "app-personium-trails",
    "started_at": "2020-06-28T14:30:41.119Z",
    "progress": "25%",
    "url": "https://alice.example/app-personium-trails/",
    "status": "installation in progress"
  },
  "unit": {
    "path_based_cellurl_enabled": false,
    "url": "https://example/"
  }
}
```

When the status value is `ready`, Box installation is complete.

Access the [Box URL acquisition](../apiref/304_Get_Box_URL.md) API when getting the Box URL from the access token with Box installed.

```text
# request
GET https://alice.example/__box


# Response
Status Code: 200

{
  "Url": "https://alice.example/app-personium-trails/"
}
```

The following screen will be displayed when Box installation is completed.

![Personium Trails Top Page](assets/getting-started/personium_trails_top.png)

From this screen, you can select the location history data (eg 2020_MAY.json) which you have to obtain from Google Takeout and upload to Personium in advance. Please follow the instructions in [Personium Trails](https://github.com/personium/app-personium-trails).

----

## Relational data (OData)

In the following screen, the data list for a specific period is acquired and displayed.

![Movement history data list](assets/getting-started/trails_locations.png)

OData is suitable for the data you want to search. Use [Entity list acquisition](../apiref/365_List_Entity.md) API of OData collection to get the data list of accommodations for a specific period. HTTP communication is as follows.

```text
# request
GET https://alice.example/app-personium-trails/index/Stay
?$filter=startTime ge 1589554800000 and startTime lt 1589641199999
&format=json

# Response
Status Code: 200
{
  "d": {
    "results": [
      {
        "__metadata": {
          "uri": "https://alice.example/app-personium-trails/index/Stay(15fa4db6e57f43a5a39b3e61eff767c0)",
          "etag": "W/\"1-1593356562389\"",
          "type": "UserData.Stay"
        },
        "__id": "15fa4db6e57f43a5a39b3e61eff767c0",
        "__published": "/Date(1593356562389)/",
        "__updated": "/Date(1593356562389)/",
        "endTime": "/Date(1589596800521)/",
        "latitudeE7": 3752*****,
        "longitudeE7": 13961*****,
        "name": "Wakaba Store",
        "placeId": "ChI********hBI",
        "startTime": "/Date(1589594150000)/"
      },
```

----

## file (WebDAV)

Each destination information and movement information is saved as a JSON format file by dividing the original data. The detail page uses the [Get File](../apiref/311_Get_WebDav) API of the WebDAV collection to get and display this file.

![Details page](assets/getting-started/trails_detail.png)

HTTP communication is as follows.

```text
# request
GET https://alice.example/app-personium-trails/locations/2020/0516/s_1589592400000.json

# Response
Status Code: 200

(Contents of JSON file)
```

----

## Data sharing

In Personium, you can share data with others by setting ACL of resources. In the sample application, by pressing a toggle on part of the movement history data, anyone can view it without authentication.

![Movement history data list](assets/getting-started/trails_locations_public.png)

At this time, [Box Level Access Control Settings](../apiref/315_Configure_Access_Control.md) API is used. HTTP communication is performed as follows.

```xml
# request
ACL https://alice.example/app-personium-trails/locations/2020/0516/s_1589592400000.json

<?xml version="1.0" encoding="utf-8" ?>
<acl xmlns="DAV:" xmlns:p="urn:x-personium:xmlns">
    <ace xmlns="DAV:" xmlns:p="urn:x-personium:xmlns">
        <principal>
            <all/>
        </principal>
        <grant>
            <privilege>
                <read/>
            </privilege>
        </grant>
    </ace>
</acl>

# Response
Status Code: 200
```

ACL settings can be confirmed by [Get file settings](../apiref/307_Get_Property.md) API.

```xml
# request
PROPFIND https://alice.example/app-personium-trails/locations/2020/0516/s_1589592400000.json

# Response
Status Code: 207

<multistatus xmlns="DAV:">
    <response>
        <href>https://alice.example/app-personium-trails/locations/2020/0516/s_1589592400000.json</href>
        <propstat>
            <prop>
                <creationdate>2020-06-29T00:02:41.816+0900</creationdate>
                <getcontentlength>2623</getcontentlength>
                <getcontenttype>application/json</getcontenttype>
                <getlastmodified>Sun, 28 Jun 2020 15:02:41 GMT</getlastmodified>
                <resourcetype/>
                <acl xml:base="https://alice.example/__role/app-personium-trails/" xmlns:p="urn:x-personium:xmlns">
                    <ace>
                        <principal>
                            <all/>
                        </principal>
                        <grant>
                            <privilege>
                                <D:read xmlns:D="DAV:"/>
                            </privilege>
                        </grant>
                    </ace>
                </acl>
            </prop>
            <status>HTTP/1.1 200 OK</status>
        </propstat>
    </response>
</multistatus>
```

[^1]: The engine script executes simple server-side logic on Personium. See [Personium Engine](../app-developer/Personium-Engine.md) for details. The template app personium-blank-app allows you to use two engine scripts, start_oauth2.js and receive_redirect.js, for use in the OAuth 2.0 authorization code flow.
