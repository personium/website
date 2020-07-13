---
id: unit_coordination
title: Unit間連携の設定方法
sidebar_label: Unit間連携の設定方法
---

## 概要

Personiumは別々のサーバインフラに⽴てられたに立てられたUnitが相互に連携しあうことが出来ることを大きな特長としています。
具体的にはUnit間の連携を設定することにより、UnitをまたいだCell間の連携が可能となります。
そのように設定しないこともできますが、Personiumのこの特長を活かしてアプリやユーザのエコシステムをUnitをまたいで共有するためこの連携設定が推奨されます。

逆に言えば、この設定を行わない限りUnitをまたいだCellの連携はできませんので注意が必要です。

Unit間の連携の設定は、Unitに以下の設定をすることにより行います。

1. Unit秘密鍵
1. Unit証明書
1. Unit証明書発行者の証明書

Unit秘密鍵についてはUnitの運営者が自身で作成し管理するものですが、Unit証明書を誰に発行してもらうかという点については３つのオプションがあります。

1. オープンソースPersoniumコミュニティに発行してもらう
1. 他のUnit証明書発行者から発行してもらう
1. 自身で自己署名Unit証明書を作りそれを使う

Unit証明書は、そのUnitが不正な主体によって運営されていないことを証明するもので、x509のPKIフレームワークによりこれを実現しています。具体的にはUnitを認証する何等かの主体がUnit証明書発行者となります。


## 連携設定の流れ

Unit証明書発行を受ける手順は、同じくx509のSSL/TLSのサーバ証明書発行を受ける手順と同じです。
具体的には以下の流れでUnit間連携設定を行います。

1. Unit（サーバ）運営者がopenssl等のツールを使って秘密鍵とCSRを作成
1. Unit運営者がCSRを証明書発行者に送付し証明書の発行を依頼
1. 証明書発行者が依頼を吟味し問題なければ証明書を発行
1. Unit運営者が発行された証明書と自身が1で作成した秘密鍵をUnitに設定

2, 3については、誰がUnit証明書発行者となるかでプロセスが変わります。


## 秘密鍵の作成

以下にopensslを使った秘密鍵作成の手順を示します。

```console
    # openssl genrsa -out unit.key 2048 -outform DER
```  
Example:)

```console
    # openssl genrsa -out unit.key 2048 -outform DER
    Generating RSA private key, 2048 bit long modulus
    ............................................................+++
    ...................................................+++
    e is 65537 (0x10001)
    -----------------------------------------------------------------------------------
```

unit.keyが作成されたことを確認します。
ここで作成されたunit.keyが秘密鍵です。

```console
    # ls -l
```

Example:)

```console
    # ls
    total 4
    -rw-r--r--. 1 root root 1675 Sep  1 20:27 unit.key
```

## CSRの作成

unit.keyを使ってCSRを作成します。以下で得られるunit.csrがCSRです。
CSR作成時に、CN項目にPersonium UnitのFQDNを設定してください。


```console
  # openssl req -new -key unit.key -out unit.csr
    > enter the required information interactively.
      * Common Name value should be the unit domain name (required)
```

Example:)

```console
    # openssl req -new -key unit.key -out unit.csr
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [XX]:
    State or Province Name (full name) []:
    Locality Name (eg, city) [Default City]:
    Organization Name (eg, company) [Default Company Ltd]:
    Organizational Unit Name (eg, section) []:
    Common Name (eg, your name or your server's hostname) []:example.com            <* Enter the unit domain name (required)
    Email Address []:
    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []:
    An optional company name []:

```



## CSRをもとに証明書の発行を受ける

### Personiumプロジェクトに依頼する場合

Personium Unitエコシステムへ参加させる場合は、PersoniumプロジェクトにUnit証明書の発行を依頼してください。

⇒[Slackコミュニティ](https://personium-io.slack.com/)の #infra / #infra_ja チャネルに依頼を出してください。
Slackコミュニティへの参加登録は[こちら](https://bit.ly/Join_Personium_Slack)からどうぞ。


### 自己発行する場合

他のUnitと連携させない設定をする場合は、自己署名のUnit証明書を設定することによりこれを行うことができます。

https://github.com/personium/ansible/tree/master/3-server_unit


## 秘密鍵と証明書の設定

発行された証明書と自身が1で作成した秘密鍵をサーバに設定します。Unit設定ファイルの以下項目の設定を行ってください。

|キー名|設定内容|
|:--|:--|
|x509.key|Unit秘密鍵ファイルのパス|
|x509.crt|Unit証明書ファイルのパス|
|x509.root|Unit証明書発行者の証明書ファイルのパス|

x509.rootについては、複数のファイルの指定が可能です。
何も指定しなければPersonium公式CAの証明書は自動的に信頼されます。(キーの定義もしない)
何等かの設定を行えばこの動作は無効化されるので、Personiumプロジェクトのエコシステムに参加
させたくない場合は、何等かの設定を行ってください。

[参照](../server-operator/unit_config_list.md)

## Unit証明書発行者となるには

オープンソースPersoniumコミュニティもUnit証明書発行者です。もし私どもの活動にご賛同いただけるのであれば、ぜひ私たちのエコシステムに参加してください。UnitにオープンソースPersoniumコミュニティ発行のUnit証明書を設定いただくことでエコシステムへの参加が可能です。

一方で、独自のエコシステムを構築したい場合は、だれでもX509の認証局を立ててUnit証明書発行者となって
独自のエコシステムを形成することができます。Unit証明書発行者となるためには以下２点が必要となります。

1. X509の認証局を立てる
1. エコシステムに参加するUnitに、Unit証明書発行者の証明書として1で立てたX509認証局の証明書を設定してもらう

この方法についての関心があり具体的な方法を知りたい方、コミュニティにお問い合わせください。
