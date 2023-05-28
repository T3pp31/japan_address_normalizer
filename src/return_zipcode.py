"""
このプログラムは入力データとデータベースの類似度スコアをつけるためのものです．
This program is used to score the similarity
between the input data and the database.
"""
import difflib

import pandas as pd
from tqdm import tqdm


def return_zipcode(x):
    """
    入力データとデータベース上の文字を比較する
    compare with input data and output data.

    parameters
    ----------
    x

    Returns
    -------
    zip_code : zipcode，提示された住所に一番近い郵便番号
    """
    # スコアを求める
    # スコアを {"市区町村字": score}に格納
    # scoreの高い順に並び替え
    # keyを使って，zipcodeを抽出
    # zipcodeを返す

    # 元となるデータベースの読み込み
    database = pd.read_csv(
        "./data/preprocessed_2023-5-28.csv", encoding="shift-jis"
    )

    # compare_score = {database['市区町村字'] : score}
    compare_score = {}

    # 入力されたデータ(x)と，databaseの見比べとスコアリング
    for database_data in tqdm(database["市区町村字"]):
        score = difflib.SequenceMatcher(None, x, database_data).ratio()
        compare_score[database_data] = score

    # 取得したスコアで一番高いものを先頭に持ってくる
    sorted_compare_score = dict(
        sorted(compare_score.items(), key=lambda x: x[1], reverse=True)
    )

    # 最高スコアを取得する(辞書の一番先頭)
    highest_score_address = next(iter(sorted_compare_score))

    matching_rows = database.loc[database["市区町村字"] == highest_score_address]

    if len(matching_rows) > 0:
        zipcode = matching_rows.iloc[0]["zip_code"]
        return zipcode
    else:
        return None


if __name__ == "__main__":
    input_data = pd.read_csv(
        "./data/preprocessed_2023-5-28.csv", encoding="shift-jis"
    )
    input_data["zip_code"] = input_data["市区町村字"].apply(return_zipcode)
    input_data.to_csv("test.csv", encoding="shift-jis", index=False)
