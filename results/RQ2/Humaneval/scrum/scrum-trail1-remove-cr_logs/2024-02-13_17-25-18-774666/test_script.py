def anti_shuffle(s):
    words = s.split(' ')
    result = ''
    for word in words:
        sorted_word = ''.join(sorted(word))
        result += sorted_word + ' '
    return result.strip()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('Hi'), 'Hi')
        self.assertEqual(function_under_test('hello'), 'ehllo')
        self.assertEqual(function_under_test('Hello World!!!'), 'Hello !!!Wdlor')

if __name__ == '__main__':
    unittest.main()