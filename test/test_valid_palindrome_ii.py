import unittest

from src.algorithms.string.valid_palindrome_ii import PalindromeII


class TestPalindromeII(unittest.TestCase):
    def setUp(self):
        self.palindrome = PalindromeII()

    def test_is_valid_palindrome(self):
        is_valid_str = self.palindrome.validate_palindrome('abba')
        self.assertEqual(is_valid_str, True)

    def test_is_invalid_palindrome(self):
        is_valid_str = self.palindrome.validate_palindrome('abcde')
        self.assertEqual(is_valid_str, False)


if __name__ == '__main__':
    unittest.main()
