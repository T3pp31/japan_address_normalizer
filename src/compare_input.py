"""
このプログラムは入力データとデータベースの類似度スコアをつけるためのものです．
This program is used to score the similarity
between the input data and the database.
"""
import difflib


def compare_input(input_data, database_data):
    """
    入力データとデータベース上の文字を比較する
    compare with input data and output data.

    parameters
    ----------
    input_data : address to be searched. 検索したい一つ住所
    database_data : database address. データベース上の一つアドレス.

    Returns
    -------
    score : similarity score between input_data and database_data.
            input_dataとdatabase_dataの類似度スコア
    """

    score = difflib.SequenceMatcher(None, input_data, database_data).ratio()

    return score
