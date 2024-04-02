import unittest
from unittest.mock import patch
from cheating_janken import cheating_janken


class TestCheatingJanken(unittest.TestCase):
    @patch("builtins.print")
    def test_user_chooses_rock(self, mock_print):
        cheating_janken("グー")
        mock_print.assert_any_call("あなたの手はグーです。")
        mock_print.assert_any_call("わたしの手はパーです。")
        mock_print.assert_any_call("わたしの勝ちです")

    @patch("builtins.print")
    def test_user_chooses_scissors(self, mock_print):
        cheating_janken("チョキ")
        mock_print.assert_any_call("あなたの手はチョキです。")
        mock_print.assert_any_call("わたしの手はグーです。")
        mock_print.assert_any_call("わたしの勝ちです")

    @patch("builtins.print")
    def test_user_chooses_paper(self, mock_print):
        cheating_janken("パー")
        mock_print.assert_any_call("あなたの手はパーです。")
        mock_print.assert_any_call("わたしの手はチョキです。")
        mock_print.assert_any_call("わたしの勝ちです")

    @patch("builtins.print")
    def test_user_chooses_invalid_input(self, mock_print):
        cheating_janken("無効な入力")
        mock_print.assert_called_once_with(
            "グー、チョキ、パーのいずれかを入力してください。"
        )
