---
id: 315_Configure_Access_Control
title: Box Level アクセス制御設定
sidebar_label: Box Level アクセス制御設定
---
## 概要
Box Level のアクセス制御機能を提供する

### 必要な権限
write-acl

### 制限事項
* ACL設定を行うと、既存のACL設定を上書きされる形で更新されます
* ACL設定を打ち消す機能（deny）
* ACLで設定出来るprivilegeの一覧取得


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}
```
または、
```
{CellURL}{BoxName}/{ResourcePath}
```

### メソッド
ACL

### リクエストクエリ
なし

### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用される|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定する|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|

### リクエストボディ
名前空間

|URI|概要|参考prefix|
|:--|:--|:--|
|DAV:|WebDAVの名前空間|D:|
|urn&#58;x-personium:xmlns|Personiumの名前空間|p:|

※ 参考prefixは以下表の可読性を高めるためのもので、このprefix文字列の使用を保証するものでも要求するものでもありません。


XMLの構造  
ボディはXMLで、以下のスキーマに従っています。  
privilegeタグ配下の権限設定の内容については、acl_model（[アクセス制御モデル](006_Access_Control.md)）を参照。

|ノード名|名前空間|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|acl|D:|要素|ACL（アクセス制御リスト）のルートを表し、1つ以上複数のaceが子となる||
|base|xml:|属性|hrefタグ内に記述するURLの基底を表し、任意の値を属性値とする。この属性は任意。||
|ace|D:|要素|ACE（アクセス制御エレメント）を表し、principalとgrantが一対で子となる|「invert」「deny」「protected」「inherited」はV1.1系未対応|
|principal|D:|要素|権限設定対象を表し、hrefまたはallが子となる||
|grant|D:|要素|権限付与設定を表し、1つ以上複数のprivilegeが子となる||
|href|D:|要素|権限設定対象ロールを表し、ロールリソースURLを入力するテキストノード|権限設定対象ロールのリソースURLを指定する acl要素内のxml:base属性の設定によって、URLを短縮する事が出来る|
|all|D:|要素|全アクセス主体権限設定||
|privilege|D:|要素|権限設定を表し、以下の要素のいづれか一つが子となる||
|read|D:|要素|参照権限||
|write|D:|要素|編集権限||
|read-properties|D:|要素|プロパティ参照権限||
|write-properties|D:|要素|プロパティ編集権限||
|read-acl|D:|要素|ACL設定参照権限||
|write-acl|D:|要素|ACL設定編集権限||
|bind|D:|要素|メンバーURL追加権限|未対応|
|unbind|D:|要素|メンバーURL削除権限|未対応|
|exec|p:|要素|サービス実行権限||
|stream-send|p:|要素|ストリームへの送信権限||
|stream-receive|p:|要素|ストリームの受信権限||


DTD表記

名前空間 D:
```dtd
<!ELEMENT acl (ace*) >
<!ELEMENT ace ((principal or invert), (grant or deny), protected?,inherited?)>
<!ELEMENT principal (href or all)>
<!ELEMENT principal (privilege*)>
<!ELEMENT href (#PCDATA)>
<!ELEMENT all EMPTY>
<!ELEMENT privilege (all or read or write or read-properties or write-properties or read-acl 
or write-acl or exec or send or receive or bind or unbind)>
<!ELEMENT read EMPTY>
<!ELEMENT write EMPTY>
<!ELEMENT read-properties EMPTY>
<!ELEMENT write-properties EMPTY>
<!ELEMENT read-acl EMPTY>
<!ELEMENT write-acl EMPTY>
<!ELEMENT bind EMPTY>
<!ELEMENT unbind EMPTY>
```

名前空間 p:
```dtd
<!ATTLIST acl requireSchemaAuthz (none or public or confidential) #IMPLIED>
<!ELEMENT exec EMPTY>   
<!ELEMENT stream-send EMPTY>   
<!ELEMENT stream-receive EMPTY>   
```

名前空間 xml:
```dtd
<!ATTLIST acl base CDATA #IMPLIED>
```

### リクエストサンプル
```xml
<?xml version="1.0" encoding="utf-8" ?>
<D:acl xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns"
       xml:base="https://cell1.unit1.example/__role/box1/"
       p:requireSchemaAuthz="public">
  <D:ace>
    <D:principal>
      <D:all/>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
    </D:grant>
  </D:ace>
  <D:ace>
    <D:principal>
      <D:href>role1</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><D:read/></D:privilege>
      <D:privilege><D:write/></D:privilege>
      <D:privilege><p:exec/></D:privilege>
    </D:grant>
  </D:ace>
</D:acl>
```


## レスポンス
### ステータスコード

|コード|メッセージ|概要|
|:--|:--|:--|
|200|OK|成功|

### レスポンスヘッダ

|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式|更新・作成時に失敗した場合のみ返却する|

### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照


## cURLサンプル

```sh
curl "https://cell1.unit1.example/box1/collection1" -X ACL -i \
-H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Accept: application/json' \
-d '<?xml version="1.0" encoding="utf-8" ?><D:acl xmlns:D="DAV:" \
xml:base="https://cell1.unit1.example/__role/box1/" xmlns:p="urn:x-personium:xmlns" \
p:requireSchemaAuthz="none"><D:ace><D:principal><D:href>role1</D:href></D:principal><D:grant>\
<D:privilege><D:read/></D:privilege><D:privilege><D:write/></D:privilege></D:grant></D:ace></D:acl>'
```
