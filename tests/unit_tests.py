import unittest
from anagrams.anagrams import anagram


class AngramTest(unittest.TestCase):
    #right test
    def test_right(self):
        self.assertEqual(anagram('a1bcd efg!h'), 'd1cba hgf!e')

    def test_not_symbol(self):
        self.assertEqual(anagram('abcde'), 'edcba')

    def test_only_str_numbers(self):
        self.assertEqual(anagram('1234'), '1234')

    def test_empty(self):
        self.assertEqual('', '')
    #wrong tests
    def test_numbers(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(anagram(123))

    def test_list(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(anagram([1, 2, 3]))
        self.assertEqual('Выражение должно содержать только строковые символы', e.exception.args[0])

    def test_dict(self):
        with self.assertRaises(TypeError) as e:
            self.assertEqual(anagram({'1': 2, 'asd': 1}))
        self.assertEqual('Выражение должно содержать только строковые символы', e.exception.args[0])


if __name__ == '__main__':
    unittest.main()
