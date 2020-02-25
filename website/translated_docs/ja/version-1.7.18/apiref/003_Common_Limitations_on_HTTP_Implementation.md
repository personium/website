---
id: version-1.7.18-003_Common_Limitations_on_HTTP_Implementation
title: PersoniumのHTTP実装に関する制限事項
sidebar_label: PersoniumのHTTP実装に関する制限事項
---


## リクエスト
### URL
最大サイズ: 50KByte
※URL サイズ = ヘッダサイズ + （URLパスサイズ × ２） + （クエリサイズ × ３）  
※参考）IE7,8の制限値は2048byte、IE9は5120byte、その他の多くブラウザは1Mbyte程度
### リクエストヘッダ
各ヘッダの上限サイズ： 4096byte （キーを含めての長さかどうかは不明）
#### Accept Encoding
gzip に対応しています。
### リクエストボディ
#### Transfer-Encoding
chunked のリクエストに対応しています。
#### Content-Encoding
gzip のリクエストに対応予定ですが未対応です。
### Time-out
60秒（リクエスト開始から、サーバがリクエストをすべて受領し終わるまでの時間）


## レスポンス
### レスポンスヘッダ
|ヘッダ名|説明|
|:--|:--|
|Transfer-Encoding|常にchunkedでレスポンスします|
|Content-Encoding|リクエストヘッダで有効なAccept-Encoding値を設定された場合、その値が入ります|
|Date|リクエストを受け付けたUTC時刻を返却します|
### レスポンスボディ
#### Transfer-Encoding
原則chunked でレスポンスを行います。
#### Content-Encoding
リクエストヘッダで有効なAccept-Encoding値を設定された場合は、ボディはその形式で圧縮エンコードされます。

