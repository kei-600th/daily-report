# Cheating Janken

以下のように実行してください。
~~~
docker-compose build

# プログラムを動かすとき
docker-compose run --rm python-cheating-janken python cheating_janken.py

# テストを動かすとき
docker-compose run --rm python-cheating-janken python -m unittest cheating_janken_test.py
~~~