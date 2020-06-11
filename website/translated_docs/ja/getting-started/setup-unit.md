---
id: setup-unit
title: Personium Unitの構築
sidebar_label: Unitの構築
---

## はじめに

本章ではPersonium Unitの構築を行います。

Personium Unitを構築するためのサーバインフラの構成や構築方法は様々な形をとることができますが、本章では入門用としてIaaS上の1台のサーバに全ての役割の持たせるall-in-one構成のPersonium UnitをAnsible Playbookで構築します。

もし、他の構成で構築する場合、[サーバソフトウェア運用者向けガイド](../server-operator/README.md)をご参照ください。

## 注意事項

Personium Unitは`https://user1.personium.example`や`https://user2.personium.example`といったユーザによって異なるサブドメインでのHTTPSアクセスを行うことを前提にしているため、以下が基本必要となります。

- WebサーバにアクセスするIPアドレスに対しての`*.personium.example`といったワイルドカードドメイン名でのDNSレコード設定
- `*.personium.example`といったワイルドカードドメイン名に対応したSSL証明書の取得と設定

上記を簡単に行うために、ローカルネットワーク上で構築するよりもパブリックIaaSとDNSサービスを使って構築することを推奨します。本章もそれを前提にした手順をとっています。

## 構築

### VMの作成

パブリックIaaSを使ってVMを作成します。以下スペックのVMで動作することを確認しています。

|項目|値|
|----|----|
|IaaS|Microsoft Azure Virtual Machines|
|OS|CentOS 7|
|サイズ|Standard B2ms (2 vcpu 数, 8 GiB メモリ)|
|OS ディスク|30 GiB|
|パブリック IP アドレス|あり|

> Personium自体はCentOS7以外のOSにおいても動作しますが、後述で使用するAnsible PlaybookがCentOS7前提のため、CentOS7系をご使用ください。

### セキュリティグループ/ファイアウォールの設定

Personium Unitにアクセスするために、作成したVMのパブリックIPアドレスに対して以下ポートのアクセスを許可するようにセキュリティグループ/ファイアウォールを設定します。

|ポート|用途|
|----|----|
|443|HTTPSアクセス|

### Ansibleを使ったPersoniumインストール

以下ドキュメントの手順を実施します。

[Personium Ansible Playbook 1-server](https://github.com/personium/ansible/tree/develop/1-server_unit)

正常に完了した場合、Personium Unitが構築されます。

### Personium Unitへのアクセス確認

ブラウザで`https://{Personium Unitのドメイン名}/`にアクセスします。以下の形式のレスポンスが表示されます。

```json
{"unit":{"path_based_cellurl_enabled":false,"url":"https:\/\/{Personium Unitのドメイン名}\/"}}
```

### Personium Unit管理のためのアクセス情報

Ansible Playbookで構築した場合、Cell作成などを行うためのUnit管理アカウントが作成されます。Unit管理アカウントについては以下ドキュメントを参照してください。

[Personium Unit管理アカウント](../server-operator/Confirm_environment_settings/#personium-%E3%83%A6%E3%83%8B%E3%83%83%E3%83%88%E7%AE%A1%E7%90%86%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88)
