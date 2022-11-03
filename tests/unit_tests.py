import unittest
from anagrams import anagram


class AnagramTest(unittest.TestCase):
    cases = [
        ('a1bcd efg!h', 'd1cba hgf!e'),
        ('abcde', 'edcba'),
        ('1234', '1234'),
        ('', ''),
    ]
    for text, reversed_text in cases:
        assert anagram(text) == reversed_text

    def test_anagram_negative_cases(self):
        for i in [123, [1, 2, 3], {'1': 2, 'asd': 1}]:
            with self.subTest(i=i):
                with self.assertRaises(TypeError) as exept_text:
                    self.assertEqual(anagram(i))
                self.assertEqual('You must use only string symbol', str(exept_text.exception))
