# Cell Level アクセス制御設定
## 概要
Cell Level のアクセス制御機能を提供する。

### 必要な権限
acl

### 制限事項
ACL設定を行うと、既存のACL設定を上書きされる形で更新されます。
* V1.0版での制限
	- ACL設定を打ち消す機能（deny）
	- ACLで設定出来るprivilegeの一覧取得


## リクエスト
### リクエストURL
```
{CellURL}
```
### メソッド
ACL

### リクエストクエリ
共通リクエストクエリ

|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|


### 共通リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|X-HTTP-Method-Override|メソッドオーバーライド機能|任意|×|POSTメソッドでリクエスト時にこの値を指定すると、指定した値がメソッドとして使用されます。|
|X-Override|ヘッダオーバライド機能|${上書きするヘッダ名}:${値}|×|通常のHTTPヘッダの値を上書きします。複数のヘッダを上書きする場合はX-Overrideヘッダを複数指定します。|
|X-Personium-RequestKey|イベントログに出力するRequestKeyフィールドの値|半角英数、-(半角ハイフン)と_(半角アンダーバー)<br>最大128文字|×|指定がない場合、PCS-${UUIDで32文字の文字列}を設定する|
### リクエストヘッダ

|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン|
### リクエストボディ
### 名前空間

|URI|概要|備考 (prefix)|
|:--|:--|:--|
|DAV:|WebDAVの名前空間|D:|
|urn&#58;x-personium:xmlns|Personiumの名前空間|p:|

※ 参考prefixは以下表の可読性を高めるためのもので、このprefix文字列の使用を保証するものでも要求するものでもありません。

### XMLの構造
ボディはXMLで、以下のスキーマに従っています。  
privilegeタグ配下の権限設定の内容については、acl_model（[アクセス制御モデル](006_Access_Control.md)）を参照。

|ノード名|Namespace|ノードタイプ|概要|備考|
|:--|:--|:--|:--|:--|
|acl|D:|要素|ACL（アクセス制御リスト）のルートを表し、1つ以上複数のaceが子となる||
|base|D:|要素|hrefタグ内に記述するURLの基底を表し、任意の値を属性値とする。||
|ace|D:|要素|ACE（アクセス制御エレメント）を表し、principalとgrantが一対で子となる<br>※プロパティ取得時、継承したACEの子にinheritedが追加される|「invert」「deny」「protected」は未対応|
|principal|D:|要素|権限設定対象を表し、hrefまたはallが子となる||
|grant|D:|要素|権限付与設定を表し、1つ以上複数のprivilegeが子となる||
|href|D:|要素|権限設定対象ロール表し、ロールリソースURLを入力するテキストノード|権限設定対象ロールのリソースURLを指定する<br>acl要素内のxml:base属性の設定によって、URLを短縮する事が出来る|
|all|D:|要素|全アクセス主体権限設定|全てのロールや認証されていないアクセス主体（Authorizationヘッダなし）に対しての設定となる|
|inherited|D:|要素|権限継承元を表し、href（権限継承元コレクションのURL）が子となる|※設定不可（プロパティ取得時にのみ付与される要素で、ACL設定時には無視される）|
|privilege|D:|要素|権限設定を表し、以下の要素のいづれか一つが子となる||
|root|p:|要素|全権限||
|auth|p:|要素|認証系管理API編集・参照権限||
|auth-read|p:|要素|認証系管理API参照権限||
|message|p:|要素|メッセージ系管理API編集・参照権限||
|message-read|p:|要素|メッセージ系管理API参照権限||
|event|p:|要素|イベント系管理API編集・参照権限||
|event-read|p:|要素|イベント系管理API参照権限||
|log|p:|要素|イベントバスのログAPI編集・参照権限||
|log-read|p:|要素|イベントバスのログAPI参照権限||
|social|p:|要素|関係系管理API編集・参照権限||
|social-read|p:|要素|関係系管理API参照権限||
|box|p:|要素|ボックス管理API編集・参照権限||
|box-read|p:|要素|ボックス管理API参照権限||
|box-install|p:|要素|Boxインストール実行権限 ※V1.2.3対応||
|box-export|p:|要素|Boxエクスポート実行権限|未対応(設定不可)|
|acl|p:|要素|ACL管理API編集・参照権限||
|acl-read|p:|要素|ACL管理API参照権限||
|propfind|p:|要素|プロパティ取得API参照権限||
|rule|p:|要素|イベント処理ルール管理API編集・参照権限||
|rule-read|p:|要素|イベント処理ルール管理API参照権限||

#### DTD表記
名前空間：D:
```dtd
<!ELEMENT acl (ace*) >
<!ATTLIST acl base CDATA #IMPLIED>
<!ELEMENT ace ((principal or invert), (grant or deny), protected?,inherited?)>
<!ELEMENT principal (href or all)>
<!ELEMENT principal (privilege+)>
<!ELEMENT href (#PCDATA)>
<!ELEMENT all EMPTY>
<!ELEMENT privilege (root or auth or auth-read or message or message-read or event or 
event-read or social or social-read or box or box-read or acl or acl-read or propfind or
rule or rule-read)>
```


名前空間:xml:
```dtd
<!ATTLIST acl base CDATA #IMPLIED>
```

名前空間：p:
```dtd
<!ELEMENT root EMPTY>
<!ELEMENT auth EMPTY>
<!ELEMENT auth-read EMPTY>
<!ELEMENT message EMPTY>
<!ELEMENT message-read EMPTY>
<!ELEMENT event EMPTY>
<!ELEMENT event-read EMPTY>
<!ELEMENT log EMPTY>
<!ELEMENT log-read EMPTY>
<!ELEMENT social EMPTY>
<!ELEMENT social-read EMPTY>
<!ELEMENT box EMPTY>
<!ELEMENT box-read EMPTY>
<!ELEMENT box-install EMPTY>
<!ELEMENT box-export EMPTY>
<!ELEMENT acl EMPTY>
<!ELEMENT acl-read EMPTY>
<!ELEMENT propfind EMPTY>
<!ELEMENT rule EMPTY>
<!ELEMENT rule-read EMPTY>
```

### リクエストサンプル
```xml
<?xml version="1.0" encoding="utf-8" ?>
<D:acl xmlns:D="DAV:" xmlns:p="urn:x-personium:xmlns" 
xml:base="https://cell1.unit1.example/__role/box1/">
  <D:ace>
    <D:principal>
      <D:all/>
    </D:principal>
    <D:grant>
      <D:privilege><p:auth/></D:privilege>
      <D:privilege><p:box/></D:privilege>
    </D:grant>
  </D:ace>
  <D:ace>
    <D:principal>
      <D:href>role</D:href>
    </D:principal>
    <D:grant>
      <D:privilege><p:root/></D:privilege>
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

|項目名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式||
### レスポンスボディ
なし

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

## cURLサンプル
```sh
curl "https://cell1.unit1.example/" -X ACL -i -H 'Authorization: Bearer AA~PBDc...(省略)...FrTjA' \
-H 'Accept: application/json' -d '<?xml version="1.0" encoding="utf-8" ?><D:acl xmlns:D="DAV:" \
xmlns:p="urn:x-personium:xmlns" xml:base="https://cell1.unit1.example/__role/box1/">  \
<D:ace><D:principal><D:href>role1</D:href></D:principal><D:grant><D:privilege><p:box-read/>\
</D:privilege><D:privilege><p:auth/></D:privilege></D:grant></D:ace></D:acl>'
```

