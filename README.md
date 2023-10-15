# study-django

Djangoプロジェクトで下記を検証するためのプロジェクト

- pyproject.tomlでのblack, isort, flake8, mypyの管理。vscodeとの同期
- uvicorn(ASGI)でのDjango Async View

# 使い方

```sh
docker compose up -d
docker compose exec app bash
python manage.py createsuperuser

# localhost:8000/: top page
# localhost:8000/admin/: admin site
```

# 計測

以下で並行処理が行えていることを確認できる

```sh
time ./time.sh
```

# Pythonの並行処理などについて簡単なまとめ

## 並列処理とは
- 順序に依存しないタスクを同時に実行すること
- 主にCPUバウンドな処理において、マルチコアCPUでそれぞれタスクを同時に処理することで全体のタスクを早く完了させる
- 数値計算、機械学習などCPUを多く使う処理で効果を発揮する

## 並行処理とは
- 待ち時間の間に別の並行可能なタスクを実行すること。厳密に言えば同時ではない。待ち時間に処理することで同時に見せかけている
- 主にI/Oバウンドな処理において、シングルコアCPUでもIO待ちの間に並行可能な他のタスクを処理することで全体のタスクを早く完了させる
- ネットワークI/O、ディスクI/O、DBのクエリ実行の待ちが多い場合に効果を発揮する

## DBクエリ実行待ちでPythonで多数のタスクを並行に実行させるには
- asyncio: Pythonで並行処理をするための機構
https://docs.python.org/ja/3/library/asyncio.html
- asyncpg: asyncioを使用してクエリ実行待ちで他タスクに委譲できるPostgreSQLクライアント
https://github.com/MagicStack/asyncpg
- uvicorn: Pythonの非同期実行用のwebサーバ
https://github.com/encode/uvicorn
