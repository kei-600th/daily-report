# Cheating Janken

## What's this?
じゃんけんの勝負ができるプログラムです。

ユーザーは「グー」「チョキ」「パー」いずれかを出すとプログラムとの勝負が始まります。

ただしプログラムはユーザーに対して必ず勝つ手を出してきます。

作者がオブジェクト指向プログラミングを学習する目的で上記のコードを書いています。

## 各ファイルの構成

* cheating_janken.py:じゃんけんの進行を行うプログラム

* hand.py:ユーザーやプログラムが出す手(グー・チョキ・パー)を記述するプログラム

* cheating_janken_test.py:上記の挙動を検証するテストコード

## 実行方法
以下のように実行してください。
~~~
docker-compose build

# プログラムを動かすとき
docker-compose run --rm python-cheating-janken python cheating_janken.py

# テストを動かすとき
docker-compose run --rm python-cheating-janken python -m unittest cheating_janken_test.py
~~~