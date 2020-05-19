---
id: README
title: Application Developer's Guide
sidebar_label: Application Developer's Guide
---

Personiumを使ってアプリケーションを開発するためのドキュメントです。

## Application structure

一般のアプリと同様、Personiumを使ってブラウザアプリ・ネイティブアプリなど様々なアプリを開発することができます。一般のアプリと違う点はユーザーのデータが各ユーザーのPDS上の領域に格納されることです。

以下の図はブラウザアプリの場合の構成例となります。

```
# 図
user -----> WEB Server
app ------> UserCell data
app ------> API Server -----> UserCell data
app ------> API Server -----> DB
```

Personiumを使ってアプリを開発する場合、上記のような構成になるように行います。

### OAuth

データアクセスの認可はOAuthに基づいて行います。

### Box

アプリのデータアクセスはBoxという領域に行います。

### WebDavとOData

データアクセスの種類としてWebDavとODataがあります。

### As WEB and API Server

Cellは基本ユーザーのデータ領域ですが、アプリ用のCellを用意することで、そこをWebサーバ・APIサーバとして使えます。

Webサーバ・APIサーバとしてのアプリCellは必須ではなく、別サーバの使用も可能です。

```
# 図
user -----> AppCell data
app ------> UserCell (EngineScript) --> UserCell Data
app ------> AppCell
app ------> AppCell (EngineScript) --> AppCell Data
```

## 開発者ツール

Unit Manager

## サンプルアプリ



## 詳細

- 認証認可
  - 全体像
  - Role/ACL詳細
  - アプリ認証詳細
  - Single Sign On
- Box
  - 概要
  - BarファイルとBoxインストール
- コレクション
  - WebDAV
  - OData
  - EngineScript
  - Stream
- CellGUIカスタマイズ
