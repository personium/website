---
id: appdev-process
title: アプリ開発の流れ
sidebar_label: アプリ開発の流れ
---

本節ではアプリ開発の流れについて説明します。

まず、アプリ開発の流れの説明の前にいくつか知っておいた方がよいことを説明します。

## OAuth 2.0 認可コードフロー

Personiumを使用したアプリの場合、アプリからのパーソナルデータへのアクセスはデータ主体Cell内のBoxに対してREST APIを通じて行います。この時、データアクセスの認可方法はOAuth 2.0の仕様に従います。OAuth 2.0のフローは種類がありますが、サンプルアプリではPDS事業者とアプリ事業者が異なる場合に採用する認可コードフローを使用します。

認可コードフローについての詳細は[認可モデル](../user_guide/003_Auth.md#アプリ認可)を参照してください。

## データ主体CellとアプリCell

認可コードフローで実装する場合、データ主体CellとアプリCellという2種類のCellを使用します。この2種類のCellは以下のように使われます。

|Cell種類|役割|
|----|----|
|データ主体Cell|データ主体のデータ管理と認可|
|アプリCell|OAuth 2.0に従ったアプリの認可とアプリ資産の格納・公開|

アプリCellは認可コードフローで以下のように使われます。

* クライアント登録: アプリCell作成によって行う
* client_id: アプリCellのURLを使用する
* client_secret: アプリCell上のアカウントを使用してアプリの認証を行い、取得する

また、アプリCell上にHTML, JavaScript, CSSといったファイルを格納し、アクセス設定を誰でも参照できるようにすることで、静的Websiteのホスティングも行えます。本節のJavaScriptによるサンプルアプリはアプリCell上でホスティングすることを想定しています。

サンプルアプリでのデータ主体CellとアプリCellの関係を表すと次の図の通りとなります。

![Cell Relation](assets/getting-started/cell_relation.png)

アプリの開発はデータ主体Cell部分とアプリCell部分に対して行います。

## Boxとbarファイルインストール

アプリはどのデータ主体Cellを使っても意図した挙動を行うために、Box上で同じデータ構造を取る必要があります。Personiumではアプリのユーザがアプリを使用する前に、データ主体Cellのデータ構造を定義するbarファイルを使ってBoxインストールを行い、アプリ固有のデータ構造をBox上に構築します。詳しくは以下ドキュメントを参照してください。

* [Boxインストール](../apiref/007_Box_install.md)
* [barファイル](../apiref/301_Bar_File.md)

データ主体Cell部分の開発はBox上のデータ構造の構築とbarファイルの出力となります。

## テンプレートアプリ

Personiumコミュニティでは[React](https://reactjs.org/)ベースのJavaScriptアプリのテンプレート及びデプロイメントツールを提供しています。

[personium-blank-app](https://github.com/personium/personium-blank-app)

本ツールを使うことで、最小限のデータ主体CellとアプリCellからカスタマイズしてオリジナルのアプリを開発することができます。また、barファイルのビルドやアプリCellへのアップロードといった開発作業を簡単にします。

### 初期構築の流れ

テンプレートアプリの初期構築の流れは以下の通りとなります。

1. ローカル開発環境へのpersonium-blank-appのclone
2. アプリCellの構築
   1. 設定ファイルの編集
   2. アプリCellへのデプロイ (`npm run deploy`の実行)
   3. アプリCell上ファイルのACL設定
3. データ主体Cellの構築
   1. barファイルのビルド (`npm build-bar`の実行)
   2. 開発用データ主体CellへのBoxインストール

具体的な手順は[personium-blank-app](https://github.com/personium/personium-blank-app)を参照してください。

> ACL設定やBoxインストールといったCell上の操作を行うのに[前節で説明したUnit Manager](./appdev-management-tool.md)が活用できます。

## アプリ開発の流れ

テンプレートアプリ構築後、以下を繰り返すことで開発を行えます。

* 開発用データ主体Cell上の開発
  1. Unit ManagerによるBox上データ構造の作成
  2. アプリの動作確認
  3. Unit Managerによるbarファイルの出力
  4. barファイルのコードリポジトリへのコミット
* アプリCell上の開発
  1. ローカル開発環境でのファイル編集(HTML/JavaScript/CSSなど)
  2. アプリCellへのデプロイ (`npm run deploy`の実行)
  3. アプリCell上ファイルのACL設定
  4. アプリの動作確認
  5. アプリCell上ファイルのコードリポジトリへのコミット

> アプリCellへのデプロイの代わりにローカル開発環境上で開発用Webサーバを起動して動作確認することもできます。その場合、`npm run debug`を実行します。

## Boxデータ構造の作成

前項の「Unit ManagerによるBox上データ構造の作成」について補足します。

Personiumではファイルデータ(WebDAV)とリレーショナルデータ(OData)の両方が使用できます。この両者では以下の違いがあります。

|データ種類|検索性|ACL設定の単位|
|--------|-----|------------|
|WebDAV|❌ 検索不可|✅ ファイル/コレクション単位で設定|
|OData|✅ クエリで検索可能|❌ コレクション単位で設定|

そのため検索させるためのデータをODataで扱い、ACL設定を行う単位の詳細情報データをWebDAVで扱うことを推奨します。

## サンプルアプリでのBoxデータ構造

参考までにサンプルアプリではBoxデータ構造を記載します。

### コレクション全体

|パス|種類|内容|
|----|----|----|
|/locations/{YYYY}/{MMdd}/s_{start_time}.json|WebDAV|滞在先詳細情報|
|/locations/{YYYY}/{MMdd}/m_{start_time}.json|WebDAV|移動詳細情報|
|/index/Stay|OData|検索用滞在先情報|
|/index/Move|OData|検索用移動情報|

元のGoogle Takeoutで取得した移動履歴データを移動・滞在先単位で分割し、分割したファイルをWebDAVで格納します。データの他者への共有するときはWebDAVの1つ1つのファイルに対して行います。また、検索を行わせるためのデータをODataに格納しています。

### OData Entity Type (Stay)

|名前|型|内容|
|----|----|----|
|name|Edm.Int32|名前|
|startTime|Edm.DateTime|開始時間|
|endTime|Edm.DateTime|終了時間|
|latitudeE7|Edm.Int32|緯度*10^7|
|longitudeE7|Edm.Int32|経度*10^7|
|placeId|Edm.String|場所Id|

### OData Entity Type (Move)

|名前|型|内容|
|----|----|----|
|name|Edm.Int32|名前|
|startTime|Edm.DateTime|開始時間|
|endTime|Edm.DateTime|終了時間|
|sLatitudeE7|Edm.Int32|移動開始緯度*10^7|
|sLongitudeE7|Edm.Int32|移動開始経度*10^7|
|eLatitudeE7|Edm.Int32|移動終了緯度*10^7|
|eLongitudeE7|Edm.Int32|移動終了経度*10^7|
