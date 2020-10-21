---
id: version-1.7.21-setup-unit
title: Personium Unitの構築
sidebar_label: Personium Unitの構築
---

## はじめに

本節ではPersonium Unitの構築について説明します。入門用としてIaaS上の1台のサーバに全ての役割の持たせるall-in-one構成のPersonium UnitをAnsible Playbookで構築します。

もし、他の構成で構築する場合、[サーバソフトウェア運用者向けガイド](../server-operator/README.md)をご参照ください。

## 注意事項

Personium Unitは`https://alice.personium.example`や`https://bob.personium.example`といったデータ主体によって異なるサブドメインでのHTTPSアクセスを行うことを前提にしているため、以下が基本必要となります。

- WebサーバにアクセスするIPアドレスに対しての`*.personium.example`といったワイルドカードドメイン名でのDNSレコード設定
- `*.personium.example`といったワイルドカードドメイン名に対応したSSL証明書の取得と設定

上記を簡単に行うために、ローカルネットワーク上で構築するよりもパブリックIaaSとDNSサービスを使って構築することを推奨します。本節もそれを前提にした手順をとっています。

## Unitの構築

### VMの作成

パブリックIaaSを使ってVMを作成します。VM作成時のパラメータの参考情報として、動作確認済みのパラメータを以下に載せます。(2020年6月現在の情報)

|項目|値|
|----|----|
|IaaS|Microsoft Azure Virtual Machines|
|OS|CentOS 7|
|サイズ|Standard B2ms (2 vcpu 数, 8 GiB メモリ)|
|OS ディスク|30 GiB|
|パブリック IP アドレス|あり|

> Personium自体はCentOS7以外のOSにおいても動作しますが、後述で使用するAnsible PlaybookがCentOS7前提のため、CentOS7系をご使用ください。

### セキュリティグループ/ファイアウォールの設定

Personium Unitの作成・アクセスするために、作成したVMのに対して以下ポートのアクセスを許可するようにセキュリティグループ/ファイアウォールを設定します。

| 方向 | ポート | ソース | 宛作 | 用途 |
|------|--------|-------|------|------|
| 受信 | 443 | 任意 | 任意 | HTTPSによるPersonium APIへのアクセス |
| 受信 | 22 | 作業マシン | 任意 | SSHによる作成したVMへのアクセス |
| 発信 | 443 | 任意 | 任意 | HTTPSによる外部リポジトリへのアクセス |
| 発信 | 80 | 任意 | 任意 | HTTPによる外部リポジトリへのアクセス |

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

[Personium Unit管理アカウント](../server-operator/Confirm_environment_settings.md#personium-unit管理アカウント)
