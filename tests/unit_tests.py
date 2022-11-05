import unittest

from anagrams import anagram
'исправлено в гит'

class AnagramTest(unittest.TestCase):
    def test_anagram_positive_cases(self):
        cases = [
            ('a1bcd efg!h', 'd1cba hgf!e'),
            ('abcde', 'edcba'),
            ('1234', '1234'),
            ('', ''),
        ]
        for text, reversed_text in cases:
            with self.subTest(text=text, reversed_text=reversed_text):
                self.assertEqual(anagram(text), reversed_text)


    def test_anagram_negative_cases(self):
        for not_str_type in [123, [1, 2, 3], {'1': 2, 'asd': 1}]:
            with self.subTest(not_str_type=not_str_type):
                with self.assertRaises(TypeError) as exept_text:
                    self.assertEqual(anagram(not_str_type))
                self.assertEqual('You must use only string symbol', str(exept_text.exception))
