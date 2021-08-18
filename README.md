# NeoUnimap

This is the Nara Universal Map on django FrameWork

## 動作環境

Python		3.8.X
PostgreSQL      13.X
PostGIS         3.1
Django          3.1.X

Pythonとデータベースは、要事前インストール。
データベースとしてPostGISを利用。MySQLは調査中。

# インストール方法

## ソースの入手

略

## ソースの展開

任意のディレクトリに展開。
Web公開する場合はWebサーバがアクセスできること。

## （必要に応じて）Python仮想環境構築

$ python -m venv venv
$ source venv/bin/activate

## Pythonパッケージのインストール

ソースを配置したディレクトリに移動したあとに以下を実行

$ pip install -r requirements.txt

## djangoの設定

- dot_env_base を .env にコピーし、設置サーバでの設定を記述
  - ファイル内でスペース、シングルクォート、ダブルクォートを使わない
  - テスト用途以外は DEBUG_FLAG=False としてデバッグモードを外す
  - 必要なデータベース設定を記載
- データベースのマイグレーション
  - python manage.py migrate
- 初期管理者の作成
  - python3.8 manage.py makesuperuser
  - 設定したユーザID/パスワードでログイン可能
- （Web公開の場合）静的ファイルの配置
  - python manage.py collectstatic

# 動作確認

## ローカルでのテスト

- 表示用データの投入
- python manage.py runserver
- ブラウザで https://localhost:8000 にアクセス

## Webサーバでの公開

### さくらのホスティングサーバの場合

準備中

### Apacheの場合

- インストール

Apache-2.4.X をインストールして起動し、動作を確認

- log/ media/ にアクセス権限を付与

chmod 777 log などでlogディレクトリに書き出せるように設定
既存ログファイルがあれば、それらへの書き込み権限を付与

- wsgi.conf の配置

wsgi.conf を設定ディレクトリ（/etc/httpd/conf.d/など）に配置
ソースディレクトリなど必要なバスを通す。

- 設定反映

Apacheを再起動などで設定反映、ブラウザでアクセス。

# 参考

* MacOS上でのPython-Django-PostgeSQL環境構築
https://qiita.com/yasushi00/items/3c944a4f63b132054b41
