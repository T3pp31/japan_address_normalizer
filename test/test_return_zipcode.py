"""
compare_inputのテスト
"""
import sys

sys.path.append("./src")
import pytest

from return_zipcode import return_zipcode

# テスト用のデータと期待される結果を定義する
test_data = [
    ("東京都千代田区飯田橋", 1020072),
    ("大阪府大阪市中央区安土町1", "5410052"),
    ("北海道札幌市中央区", "0600000"),
    ("神奈川県横浜市西区赤門町", "2200034"),
    ("福岡県福岡市博多区青木", "8120851"),
    # 他のテストデータを追加することもできます
]


@pytest.mark.parametrize("input_data, expected", test_data)
def test_return_zipcode(input_data, expected):
    # テスト対象の関数を呼び出す
    result = return_zipcode(input_data)
    # 結果と期待値を比較する
    assert result == expected
