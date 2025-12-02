def anti_shuffle(s):
    def rearrange_characters_in_word(word):
        return ''.join(sorted(word))

    if not s:
        return s

    if not isinstance(s, str):
        return "Invalid input"

    words = s.split()
    ordered_words = [rearrange_characters_in_word(word) for word in words]
    return ' '.join(ordered_words)
import unittest

class Test(unittest.TestCase):
    def test_anti_shuffle(self):
        self.assertEqual(anti_shuffle('Hi'), 'Hi')
        self.assertEqual(anti_shuffle('hello'), 'ehllo')
        self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

if __name__ == '__main__':
    unittest.main()