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
