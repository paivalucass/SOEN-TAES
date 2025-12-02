def anti_shuffle(s):
    return ' '.join([''.join(sorted(word)) for word in s.split()])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('Hi'), 'Hi')
        self.assertEqual(function_under_test('hello'), 'ehllo')
        self.assertEqual(function_under_test('Hello World!!!'), 'Hello !!!Wdlor')

if __name__ == '__main__':
    unittest.main()