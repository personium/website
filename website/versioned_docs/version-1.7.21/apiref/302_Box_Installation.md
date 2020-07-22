---
id: version-1.7.21-302_Box_Installation
title: Install Box
sidebar_label: Install Box
original_id: 302_Box_Installation
---

## Overview

Install the Box in the specified path using the bar file.For the bar file format, see "[ bar file ](301_Bar_File.md)".  
Since this API employs the asynchronous communication method, this API immediately restores after accepting Box installation.  
Therefore, to check the Box installation status, use the following API.

* [Box metadata acquisition](303_Progress_of_Bar_File_Installation.md) If Box installation terminates abnormally, you can refer to the cause of the error by checking the Box installation status with this API. Below is a method of calling from acceptance at the client to completion of processing.

```
Example call of Box installation (when polling on client is set to 30 seconds)
 1. Box installation reception
    -- MKCOL /{cell}/{box}
 2. Box Installation status check
    -- GET /{cell}/{box}  -> Returned "during processing".
    -- 30 seconds polling
 3. GET /{cell}/{box}  -> Returned by "processing completion".
 *It loops the above process 2 and polls until the process is completed.
```

### Required Privileges

box-install

### Restrictions

#### Box installation target Box restriction

* If you already have a Box with the same name, you can not install Box.
* If a Box with the same scheme URL already exists, you can not install Box.
* You can not install Box in the main box.

#### bar file limit

* The file size of the Box installable bar file is limited to the following.  
    When exceeding the upper limit value, you can not install Box.
    * File size of bar file: 100MB
    * Before compression file size of entry in bar file: 10MB

#### Box installation log detailed limit

* The details of log of Box installation is output to EventBus of Cell to which Box installation target Box belongs. following \*1
    * Therefore, when referring to log details, refer to using the log file acquisition API.
    * In order to use the log file acquisition API, the authority of "log-read" is necessary.
    * Because event logs other than Box installation also mix, it is necessary to filter by the "RequestKey" field value.
    * The "Type" field value obtains the "Requestkey" field value of "boxinstall" and filters it.

#### Other restrictions

* During the Box installation process, you can not operate data on subordinate resources including Box to be installed.
* Do not roll back if an error occurs during Box installation.

##### \*1 Box installation log detailed format

|State|"Type"|"Object"|"Info"|
|:--|:--|:--|:--|
|Box installation reception|boxinstall|BoxURL|Response Code|
|Box installation process in progress|PL-BI-1000|BoxURL|Bar installation started.|
||PL-BI-1001|Entry path in bar file|Installation started.|
||PL-BI-1002|Entry path in bar file|Installation processing.|
||PL-BI-1003|Entry path in bar file|Installation completed.|
||PL-BI-1004|Entry path in bar file|Installation failed({cause}).|
||PL-BI-1005||Unknown error({cause}).|
|Box Installation Complete|PL-BI-0000|BoxURL|Bar installation completed.|
||PL-BI-0001|BoxURL|Bar installation failed({cause}).|

##### Processing code

|Processing code|Description|
|:--|:--|
|PL-BI-0000|Box installation complete (normal termination)|
|PL-BI-0001|Box installation complete (abnormal termination)|
|PL-BI-1000|Box installation start|
|PL-BI-1001|Bar file entry start installation|
|PL-BI-1002|Bar file entry installation processing|
|PL-BI-1003|Bar file entry installation completed (normal termination)|
|PL-BI-1004|Bar file entry installation completed (abnormal termination)|
|PL-BI-1005|Internal error|


## Request

### Request URL

```
{CellURL}{BoxName}
```

### Request Method

MKCOL

### Request Query

|Query Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|p_cookie_peer|Cookie Authentication Value|The cookie authentication value returned from the server during authentication|No|Valid only if no Authorization header specified<br>Specify this when cookie authentication information is to be used|

### Request Header

|Header Name|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|Method override function|User-defined|No|If you specify this value when requesting with the POST method, the specified value will be used as a method.|
|X-Override|Header override function|${OverwrittenHeaderName}:${Value} override} $: $ {value}|No|Overwrite normal HTTP header value. To overwrite multiple headers, specify multiple X-Override headers.|
|X-Personium-RequestKey|RequestKey field value output in the event log|Single-byte alphanumeric characters, hyphens ("-"), and underscores ("_")<br>Maximum of 128 characters|No|When not specified, default value given with ${4 digits}_${22 digits} Base64url characters format representing an UUID for each request|
|Authorization|Specifies authentication information in the OAuth 2.0 format|Bearer {AccessToken}|No|* Authentication tokens are the tokens acquired using the Authentication Token Acquisition API|
|Content-Type|Specifies the request body format|application/zip|Yes||
|Content-Length|Specify the size of the request body|Half-width number|No||

### Request Body

|Overview|Effective Value|Required|Notes|
|:--|:--|:--|:--|
|Specify the bar file to install as binary in the request body|Format specified in the Content-Type header|Yes|bar file: Zip file format|

For the file structure of the bar file, see the [ bar file ](301_Bar_File.md).


## Response

### Response Code

|Code|Message|Overview|Notes|
|:--|:--|:--|:--|
|202|Accepted|Process acceptance success||

### Response Header

|Header Name|Overview|Notes|
|:--|:--|:--|
|Location|URL for Box metadata acquisition API||
|Access-Control-Allow-Origin|Cross domain communication permission header|Return value fixed to "*"|
|X-Personium-Version|API version that the request is processed|Version of the API used to process the request|

Location sample

```
Location: https://cell1.unit1.example/box1
```

For details of URL for [Box metadata acquisition API](303_Progress_of_Bar_File_Installation.md), see Box metadata acquisition.

### Response Body

None

### Error Messages

Refer to [Error Message List](004_Error_Messages.md)

### Response Sample

```
Location: {CellURL}{BoxName}
```

For details of URL for [Box metadata acquisition API](303_Progress_of_Bar_File_Installation.md), see Box metadata acquisition.

## cURL Command

```sh
curl "https://cell1.unit1.example/box1" -X MKCOL -i -H 'Content-type: application/zip' \
-H 'Authorization: Bearer AA~PBDc...(snip)...FrTjA' -H 'Accept: application/json' \
-T "/tmp/sample.bar"
```
