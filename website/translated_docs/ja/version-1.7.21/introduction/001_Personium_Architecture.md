---
id: version-1.7.21-001_Personium_Architecture
title: Personiumのアーキテクチャ
sidebar_label: Personiumのアーキテクチャ
---

## 基本となる3階層のオブジェクト

Personiumはデータ主体中心のICT実現のため以下3階層の基本オブジェクトを定義しています。

![3階層オブジェクト](assets/3LayerStructure.png "3階層オブジェクト")

|名称|概要|URL例|
|:--|:--|:--|
|Unit|多数のCellをホストするサーバ|https&#58;//personium.example/|
|Cell|データ主体ごとのデータストア|https&#58;//john.personium.example/|
|Box|アプリケーション毎のデータ領域|https&#58;//john.personium.example/schedule/|

### Unit

* Unitは、一意のFQDNを持つPersoniumを実行するシステムインフラストラクチャです。
* Personiumは独自の分散アーキテクチャを採用しているため、Unit間の関係を作成し、それに基づいて特権を与えることが可能です。
* Unitでは、複数のCellを作成することができます。

### Cell

* Cellは、データ主体ごとのData Storeです。個人で使う場合はPDS(Personal Data Store)となります。
* Personiumでは、データ主体という概念を人のみでなく組織やモノなどにも拡張したモデル化を行っているため、組織やモノのデータストアとしても使うことが可能です。
* 各Cellは、マルチテナント・モデルで異なるテナントであるかのように独立しています。
* Cellは以下の機能を提供します。

  * 認証と承認
  * アクセス制御
  * アプリケーション用データストア（Box）
  * イベント処理、メッセージング、スクリプト実行

### Box

* Boxは、アプリケーション用のデータストアです。
* Boxには、以下のデータを格納できます。

  * ディレクトリ
  * ファイルオブジェクト
  * ODataデータサービス

## オープン標準に基づく仕様

Personiumは様々なオープン標準をベースにこれを拡張したり組み合わせて構築されています。

* 認可のためのOAuth2.0
* ファイル操作のためのWebDAV
* リレーショナルデータのOData

![Personiumの仕様](assets/interface.png)
