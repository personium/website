---
id: version-1.7.21-368_Entity_Bulk_Operations
title: Entity一括操作($batch)
sidebar_label: Entity一括操作($batch)
---
## 概要
ODataEntityに対して、一覧取得や一件取得、登録、更新、削除といった一括操作を行う
### 必要な権限
* 一覧取得・一件取得  
	read
* 登録・更新・削除  
	write

### 制限事項
* $batch制限事項
	- 「GET」のリクエストクエリは未対応
	- 一覧取得を実行した場合、ランダムに10件返却する
	- NavigationProperty経由の「GET」は、未対応
	- $linksの「PUT」「GET」「DELETE」は、未対応(501を返却)


## リクエスト
### リクエストURL
```
{CellURL}{BoxName}/{ODataCollecitonName}/$batch
```
|パス|概要|
|:--|:--|
|{CellName}|セル名|
|{BoxName}|ボックス名|
|{ODataCollecitonName}|コレクション名|
### メソッド
POST
### リクエストクエリ
|クエリ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|p_cookie_peer|クッキー認証値|認証時にサーバから返却されたクッキー認証値|×|Authorizationヘッダの指定が無い場合のみ有効<br>クッキーの認証情報を利用する場合に指定する|
### リクエストヘッダ
|ヘッダ名|概要|有効値|必須|備考|
|:--|:--|:--|:--|:--|
|Authorization|OAuth2.0形式で、認証情報を指定する|Bearer {AccessToken}|×|※認証トークンは認証トークン取得APIで取得したトークン テスト未実施|
|Content-Type|リクエストボディの形式を指定する|multipart / mixed; boundary = {Boundary}|○|省略時は[multipart/mixed]として扱う 　{Boundary}に使用可能な文字種：半角英数大小文字 '()+_,-./:=?<br>未対応|
### リクエストボディ
バッチ処理内容をMIMEのマルチパートデータ形式でリクエストボディに指定する
バッチ処理の最大処理件数は、1000件まで可能  
バッチ処理には、コンテキスト取得の「クエリーオペレーション」と、コンテキスト登録・更新・削除の「チェンジセット」がある  
以下にリクエストパラメータの記述方法を説明する
```
(1)		--{バウンダリー文字列}
(2)		クエリーオペレーション or チェンジセット
(3)		--{バウンダリー文字列}
(4)		クエリーオペレーション or チェンジセット
(5)		--{バウンダリー文字列}--

(1) 開始バウンダリー文字列「--{バウンダリー文字列}」を指定する
(2) クエリーオペレーション、またはチェンジセットを指定する
(3) (4)リクエストをバウンダリー文字列「--{バウンダリー文字列}」で区切ることで、複数指定が可能となる
(5) 終了バウンダリー文字列「--{バウンダリー文字列}--」を指定する
```
* クエリーオペレーション  
	指定したコンテキストを取得する  
	以下にクエリーオペレーションの記述方法を説明する  
	※「GET」のリクエストクエリは未対応

```
(1)		Content-Type: application/http
(2)		Content-Transfer-Encoding:binary
(3)		
(4)		GET :path
(5)		:request_header

(1) Content-Type を application/httpにて指定する
(2) Content-Transfer-Encoding を binaryにて指定する
(3) 空行を指定する
(4) リクエストメソッド「GET」とパス（:path）を指定する
	:pathにはEntity情報取得対象のパスを指定する
	詳細は「Entity取得」の「リクエストURI」を参照
(5) :request_headerにはリクエストヘッダを指定する
	リクエストヘッダは、指定なし、もしくは1つ以上指定が可能
```
* チェンジセット  
	指定したコンテキストの登録・更新・削除をする  
	登録・更新・削除の処理内容をMIMEのマルチパートデータで指定する  
	以下にチェンジセットの記述方法を説明する

```
(1)		Content-Type: multipart/mixed; boundary={チェンジセットバウンダリー文字列}
(2)		Content-Length: XXX
(3)		
(4)		--{チェンジセットバウンダリー文字列}
(5)		Content-Type: application/http
(6)		Content-Transfer-Encoding: binary
(7)		
(8)		:method :path HTTP/1.1
(9)		:request_header
(10)
(11)　　　　:data
(12)
(13)	   --{チェンジセットバウンダリー文字列}--

(1) Content-Type を multipart/mixedにて指定する
	{チェンジセットバウンダリー文字列}に使用可能な文字種は「リクエストヘッダ」を参照
(2) Content-Length を指定するXXXにはチェンジセットのContent-Lengthを指定する
(3) 空行を指定する
(4) 開始チェンジセットバウンダリー文字列「--{チェンジセットバウンダリー文字列}」を指定する
(5) Content-Type を application/httpにて指定する
(6) Content-Transfer-Encoding を binaryにて指定する
(7) 空行を指定する
(8) リクエストメソッド（:method）とパス（:path）とHTTPのVersion「HTTP/1.1」を指定する
	:methodにはリクエストメソッド「POST」「PUT」「DELETE」のいずれかを指定する
	:pathにはEntity登録・更新・削除の処理対象のパスを指定する
(9) :request_headerにはリクエストヘッダを指定する
	リクエストヘッダは、指定なし、もしくは1つ以上指定が可能
(10) 空行を指定する
(11) リクエストメソッド「POST」「PUT」の場合には:dataに登録・更新対象のデータをJSON形式にて指定する
(12) リクエストメソッド「POST」「PUT」の場合には空行を指定する
(13) 終了チェンジセットバウンダリー文字列「--{チェンジセットバウンダリー文字列}--」を指定する
	チェンジセットバウンダリー文字列からチェンジセットバウンダリー文字列までが１つのリクエスト情報となり、
	リクエストをチェンジセットバウンダリー文字列で区切ることで、複数指定が可能
```
### Request Path
* {EntitySet名}
* {EntitySet名}('{\__id}')
* {EntitySet名}('{\__id}')/{NavigationProperty名}
* {EntitySet名}('{\__id}')/$links/{NavigationProperty名}

### メソッド
POST, GET, PUT, DELETE
### Request Queries
未対応
### リクエストヘッダ
ユーザデータの仕様に従う
### リクエストボディ
ユーザデータの仕様に従う
### リクエストサンプル
次に示すのは、以下の流れでコンテキストを取得・登録・更新・削除する場合のリクエストの例を示す
* 「ID:0000」を取得
* 「ID:0000、Name:田中 太郎」で登録
* 「ID:0000、familyName:田中、givenName:太郎」で更新
* 「ID:0000」を取得
* 「ID:0001、Name:太郎ログ」をNavigationProperty経由で登録
* 「ID:0001」を削除
* 「ID:0000」を削除

```
--batch_31e84e14-28b9-4741-903f-b955f2a1b853
Content-Type: application/http
Content-Transfer-Encoding:binary

GET entity-type1('0000')
Accept-Encoding: gzip
Accept: application/json
Content-Length: 0
--batch_31e84e14-28b9-4741-903f-b955f2a1b853
Content-Type: multipart/mixed; boundary=changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159
Content-Length: 608

--changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159
Content-Type: application/http
Content-Transfer-Encoding: binary

POST entity-type1
Content-Type: application/json
Content-Length: 41

{"__id":"0000","Name":"田中 太郎"}

--changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159
Content-Type: application/http
Content-Transfer-Encoding: binary

PUT entity-type1('0000')
Content-Type: application/json
Content-Length: 87
If-Match: *

{"__id":"0000","Name":"田中 太郎","familyName":"田中 ","givenName":"太郎"}

--changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159--
--batch_31e84e14-28b9-4741-903f-b955f2a1b853
Content-Type: application/http
Content-Transfer-Encoding:binary

GET entity-type1('0000')
Accept-Encoding: gzip
Accept: application/json
Content-Length: 0
--batch_31e84e14-28b9-4741-903f-b955f2a1b853
Content-Type: multipart/mixed; boundary=changeset_d4883767-a06e-4632-9608-ae952b443dfc
Content-Length: 686

--changeset_d4883767-a06e-4632-9608-ae952b443dfc
Content-Type: application/http
Content-Transfer-Encoding: binary

POST entity-type1('0001')/_log
Content-Type: application/json
Content-Length: 37

{"__id":"0001","Name":"太郎ログ"}

--changeset_d4883767-a06e-4632-9608-ae952b443dfc
Content-Type: application/http
Content-Transfer-Encoding: binary

DELETE entity-type1('0001')/_log
Content-Length: 0
If-Match: *
--changeset_d4883767-a06e-4632-9608-ae952b443dfc
Content-Type: application/http
Content-Transfer-Encoding: binary

DELETE entity-type1('0000')
Content-Length: 0
If-Match: *
--changeset_d4883767-a06e-4632-9608-ae952b443dfc--
--batch_31e84e14-28b9-4741-903f-b955f2a1b853--
```


## レスポンス
### ステータスコード
202
### レスポンスヘッダ
|ヘッダ名|概要|備考|
|:--|:--|:--|
|Content-Type|返却されるデータの形式|正常に$batch処理ができた場合：multipart/mixed; boundary={Boundary}|
|DataServiceVersion|ODataのバージョン情報|正常にEntityが作成できた場合のみ返却する|
### レスポンスボディ
レスポンスサンプル参照

### エラーメッセージ一覧
[エラーメッセージ一覧](004_Error_Messages.md)を参照

### レスポンスサンプル
次に示すのは、上記のリクエストパラメータの例を実行した場合のレスポンスの例を示す
* 「ID:0000」を取得
* 「ID:0000、Name:田中 太郎」で登録
* 「ID:0000、familyName:田中、givenName:太郎」で更新
* 「ID:0000」を取得
* 「ID:0001、Name:太郎ログ」をNavigationProperty経由で登録
* 「ID:0001」を削除
* 「ID:0000」を削除

```
--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX
Content-Type: application/http

HTTP/1.1 404 Not Found
Content-Type: application/json
Content-Length: 48
DataServiceVersion: 2.0

{
  "error": {
    "code": "404",
    "message": "Not Found"
  }
}

--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX
Content-Type: multipart/mixed; boundary=changeset_qPJh1ATATNykjJT8ocPE5MJE3QzMBS19ljS

--changeset_qPJh1ATATNykjJT8ocPE5MJE3QzMBS19ljS
Content-Type: application/http
Content-Transfer-Encoding: binary
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 425
DataServiceVersion: 2.0
Location: http://unit1.example:50280/api/context/xxx-ah,http%253A%252F%252FUnitFQDN%252Fds%252Fabc-web
/odata/user('0000')
{
  "d": {
    "Results": {
      "__metadata": {
        "uri": "http://unit1.example/api/context/xxx-ah,http%253A%252F%252FUnitFQDN%252Fds%252Fvet-web
/odata/user('0000')"
        "etag": "W/\"1-1488184348000\"",
        "type": "UserData.user",
      },
      "__id": "0000",
      "__published": "/Date(1488184348000)/",
      "__updated": "/Date(1488184348000)/",
      "name": "田中 太郎"
      }
    }
  }
}

--changeset_qPJh1ATATNykjJT8ocPE5MJE3QzMBS19ljS--
--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX
Content-Type: multipart/mixed; boundary=changeset_mry0iPNyKqKONtK237cBbGHUQhNgwIxlg70

--changeset_mry0iPNyKqKONtK237cBbGHUQhNgwIxlg70
Content-Type: application/http
Content-Transfer-Encoding: binary
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 0
DataServiceVersion: 2.0

--changeset_mry0iPNyKqKONtK237cBbGHUQhNgwIxlg70--
--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX
Content-Type: application/http

HTTP/1.1 200 OK
Content-Length: 457
ETag: W/"1-1488184348000"
DataServiceVersion: 2.0
Content-Type: application/json
{
  "d": {
    "results": {
      "__metadata": {
        "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1('0000')"
        "etag": "W/\"1-1370248522812\"",
        "type": "UserData.user",
      },
      "__id": "0000",
      "__published": "/Date(1370248522812)/",
      "__updated": "/Date(1370248522812)/",
      "name": "田中 太郎",
      "_log": {
        "__deferred": {
          "uri": "https://cell1.unit1.example/box1/odata-collection1/entity-type1
('0000')/_log"
        }
      }
    }
  }
}

--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX
Content-Type: multipart/mixed; boundary=changeset_wtsoeMGaDT6vDVM8QooqoLGEH8s6nHcrh6C

--changeset_mry0iPNyKqKONtK237cBbGHUQhNgwIxlg70
Content-Type: application/http
Content-Transfer-Encoding: binary
HTTP/1.1 201 Created
Content-Type: application/json
Content-Length: 0
DataServiceVersion: 2.0

--changeset_d4883767-a06e-4632-9608-ae952b443dfc
Content-Type: application/http
Content-Transfer-Encoding: binary
HTTP/1.1 204 No Content
Content-Type: application/json
Content-Length: 0
DataServiceVersion: 2.0

--changeset_wtsoeMGaDT6vDVM8QooqoLGEH8s6nHcrh6C
Content-Type: application/http
Content-Transfer-Encoding: binary
HTTP/1.1 204 No Content
Content-Type: application/json
Content-Length: 0
DataServiceVersion: 2.0
--changeset_wtsoeMGaDT6vDVM8QooqoLGEH8s6nHcrh6C--
--batch_AI6AVj7wPaHhKrBkYqBmA78weSj3u848CuX--
```


## cURLサンプル

curlコマンド
```sh
curl "https://cell1.unit1.example/box1/odata-collection1/\$batch" -X POST -i -H \
'Authorization: Bearer AA~PBDc...(省略)...FrTjA' -H 'Content-Type:multipart/mixed; boundary=\
batch_XAmu9BiJJLBa20sRWIq74jp2UlNAVueztqu' --data-binary @sample.txt
```
sample.txt
```
--batch_XAmu9BiJJLBa20sRWIq74jp2UlNAVueztqu
Content-Type: application/http
Content-Transfer-Encoding:binary

GET entity-type1('{100-1_20101108-111352093}')
Authorization: Bearer AA~PBDc...(省略)...FrTjA
--batch_XAmu9BiJJLBa20sRWIq74jp2UlNAVueztqu
Content-Type: multipart/mixed; boundary=changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159
Content-Length: 608

--changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159
Content-Type: application/http
Content-Transfer-Encoding: binary

POST entity-type1
Content-Type: application/json
Content-Length: 41

{"__id":"100","Name":"田中 太郎"}

--changeset_76c10b01-3eaf-49c2-bdd7-9fe90df24159--
--batch_XAmu9BiJJLBa20sRWIq74jp2UlNAVueztqu--
```

