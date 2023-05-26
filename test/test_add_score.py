"""
compare_inputのテスト
"""
import sys

sys.path.append("./src")
from add_score import compare_input


def test_add_score():

+    """
+    This function tests the functionality of the compare_input function. It compares input_data
+    with database_data and checks if they are equal. If they are equal, it sets the score to 1.0
+    and asserts that the score is equal to expected_score. This function does not take any
+    parameters and does not return anything.

+    Compares two strings and returns a score of how similar they are.
+
+    Args:
+        input_data (str): A string to compare.
+        database_data (str): A string to compare the input_data against.
+
+    Returns:
+        float: A score between 0.0 and 1.0, where 1.0 means the strings are identical.
+    """

    input_data = "東京都渋谷区恵比寿1-1-1"
    database_data = "東京都渋谷区恵比寿1-1-1"
    expected_score = 1.0

    score = add_score(input_data, database_data)
    assert score == expected_score
