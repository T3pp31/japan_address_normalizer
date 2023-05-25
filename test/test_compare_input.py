"""
compare_inputのテスト
"""
import sys

sys.path.append("./src")
from compare_input import *


def test_compare_input():
    input_data = "東京都渋谷区恵比寿1-1-1"
    database_data = "東京都渋谷区恵比寿1-1-1"
    expected_score = 1.0

    score = compare_input(input_data, database_data)
    assert score == expected_score
