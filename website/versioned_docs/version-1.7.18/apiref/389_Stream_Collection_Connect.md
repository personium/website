---
id: version-1.7.18-389_Stream_Collection_Connect
title: Web Socket connection to Stream Collection
sidebar_label: Web Socket connection to Stream Collection
original_id: 389_Stream_Collection_Connect
---

## Overview
You can receive the data sent to the topic of Stream Collection in real time.  
This API first requests transmission of an access token. Allows connection only when the corresponding token has topic receive authority.

### Required Privileges
* read : For confirmation of the existence of topic
* stream-receive : To receive data from topic

## Connection and session start

### Connection endpoint URL
```
    wss://{CellName}.{UnitFQDN}/__topic/{BoxName}/{Path}
```
or
```
    wss://{UnitFQDN}/{CellName}/__topic/{BoxName}/{Path}
```

{Path} specifies the path when sending Stream Collection, excluding {CellName} and {BoxName}, and changing "/" to ".".  
For example, the URL when sending
```
    https://cell1.unit1.example/box1/stream-collection1/topic/name
```
when the WebSocket connection is
```
    wss://cell1.unit1.example/__topic/box1/stream-collection1.topic.name
```
it becomes.

First, please connect to the above URL by WebSocket. It will be in the state which accepts an access token. In this state, sending any message other than sending access token has no meaning.

### Session start by sending access token

#### Request message

Start an event bus connection session by sending an authorized access token in the following format.  

    {"AccessToken":"AA~91WT0GNoVGFHJFQ.......e"}

#### Response message

If it is a valid token, the following response is returned, and the session will be started.

    {"Response":"AccessToken", "Result":"Success", "ExpiresIn":3600, "Timestamp":1518612600}

If the token is invalid or the token does not have the required authority, the following response is returned, and the WebSocket connection is disconnected.

    {"Response":"AccessToken", "Result":"Error", "Reason":"Token inactive", "Timestamp":1518612600}


## Communication after session start

After the session is established, the client can send the following command as a request message.

* Retransmission of access token

You can extend the session expiration date by sending a new access token with the access token send command.

As soon as you send the request message, the response message will be returned.
If there is a problem with the request message, an error response message will be returned and the WebSocket connection will be disconnected.

## Receive data

When data is sent to topic, data in JSON format is sent to the client.  

    {
      "From":"{CellURL}", 
      "Body":{data}
    }

In From, CellURL of Cell which sent data to topic is set. The sent data is set to Body.  
For example,
```
{"hoge":"testmessage", "flag":true}
```
is sent from cell1 (https: //cell1.unit1.example/), 
```
{"From":"https://cell1.unit1.example/", "Body":{"hoge":"testmessage", "flag":true}}
```
receive.

## Error response message

    {"Response": "${CorrespondingRequest}", "Result":"Error", "Reason": "${ErrorMessage}"}

|Error Message|Description|
|:--|:--|
|Invalid message|When the request message is invalid|
|Token inactive|When the token is invalid|
|Session expired|When the token has expired. Response is returned only at the time of request. CorrespondingRequest will be Unknown.|

## Web Socket Spec Details

|Item|Spec|
|:--|:--|
|Protocol|Sec-WebSocket-Version 13(RFC 6455)|
|Message format|JSON|
|ping/pong|"ping" will be sent from the Cell every one minutes.|

* Connection will be closed if client fails to respond "pong" against the "ping" from the Cell 10 times.
* Major Web Browsers automatically responds "pong" in their WebSocket client implementations. 
