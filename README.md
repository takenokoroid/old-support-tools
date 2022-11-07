# old-support-tools

## Flaskで作成するレガシーな構成のシステムを作成する

### ファイル構成
```
.
├── README.md
├── docker-compose.yml
└── webApp
    ├── Dockerfile
    ├── entrypoint.sh: DBの準備が整っているかをDBにリクエストを送ることでチェックするshellscript
    ├── flaskApp
    │   ├── __init__.py: mainファイル(ここは完全にテスト作成。DB設定などを分けたほうが良い)
    │   ├── config.py: db設定を管理するconfigファイル
    │   ├── static
    │   │   ├── css
    │   │   │   └── main.css: css
    │   │   └── javascript
    │   │       └── main.js: javascript
    │   └── templates
    │       └── index.html: テンプレートhtml
    ├── manage.py: flaskのコマンドを制御するためのファイル。
    └── requirements.txt: pythonのライブラリのインストール用のファイル
```

### 環境構築の参考サイト

[Dockerizing Flask with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)

↑とりあえず、開発環境まで環境構築したこのURL見れば何のファイルが何の意味があるのかがわかるはず.本番時はguncornなどの設定とNginxの設定が必要

[Docker & Flaskな環境構築(1) - Flask開発環境を作って触ってみた編 -](https://ameblo.jp/kazusa-g/entry-12592477686.html)

↑テンプレートやCSSの書き方の参考

[jQueryでのValidationの使い方を紹介！Validationを正しく使いこなそう!](https://www.fenet.jp/dotnet/column/language/6662/)

↑jQueryのバリデーション方法の参考

[Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html)

↑FlaskのBootstrapの導入

### 立ち上げ方法


dockerの立ち上げ(自動的にpostgresなどが立ち上がりつながるはず)
```
docker-compose up -d --build
```

dockerのdbmigration(modelを修正してください)
```
docker compose exec web python manage.py create_db
```

psqlでpostgresの中に入る
```
docker-compose exec db psql --username=hello_flask --dbname=hello_flask_dev
```