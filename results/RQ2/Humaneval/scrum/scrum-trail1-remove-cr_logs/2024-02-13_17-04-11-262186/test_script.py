def anti_shuffle(s):
    words = s.split(' ')
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))
        ordered_words.append(ordered_word)
    return ' '.join(ordered_words)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('Hi'), 'Hi')
        self.assertEqual(function_under_test('hello'), 'ehllo')
        self.assertEqual(function_under_test('Hello World!!!'), 'Hello !!!Wdlor')

if __name__ == '__main__':
    unittest.main()