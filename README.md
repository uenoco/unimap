# NeoUnimap

This is the Nara Universal Map on django FrameWork

## 動作環境

Apache		2.4.X
Python		3.9.X
Django          3.1.X
PostgreSQL      11.1

データベースとしてPostGISを利用。MySQLは調査中

# インストール方法

## ソースの入手

略

## ソースの展開

任意のディレクトリに展開。Web公開する場合はWebサーバがアクセスできること。

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

## Weサーバのテスト

### Apacheの設定

- log/ にアクセス権限を付与

chmod 777 log などでlogディレクトリに書き出せるように設定
既存ログファイルがあれば、それらへの書き込み権限を付与

- wsgi.conf の配置

wsgi.conf を設定（/etc/httpd/conf.d/など）に配置し、設置したディレクトリにパスを通す

- Apache を再起動

再起動後ブラウザでアクセス





