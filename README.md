# japan_address_normalizer

# どのような問題を解決するか

日本の住所データはさまざまな問題を抱えている．
高と髙，ケとヶなど，文字のばらつきが多い．
本リポジトリでは，住所を整形するライブラリを作成し公開する予定である．

# 処理の流れ

入力情報の正規化
↓
作成したデータベースと入力情報で差分を計算する
↓
一番もっともらしいものの郵便番号を付与する
↓
その郵便番号の住所を適用する
↓
綺麗になる

# コード規約

isort, black, flake8を使いコードを自動整形するようにする．
github actionsでpylintを行う
japan_address_normalizerからpython3でコードを実行できるように，ファイルパスは絶対パス表記で行うこと

# poetryの使い方

[poetryの使い方](https://qiita.com/ksato9700/items/b893cf1db83605898d8a)

ポエトリーに入る時は ```$ poetry shell```を実行
ポエトリーに入れない時は，自分のPythonバージョンがあってない可能性．
今回はPython3.11.0~を利用

ライブラリを追加したい時は ```$ poetry add 'package_name'```を実行
