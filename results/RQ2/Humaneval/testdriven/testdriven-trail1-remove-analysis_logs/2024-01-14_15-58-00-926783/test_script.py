def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return [word.strip() for word in txt.split(',')]
    else:
        count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
        return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test('Hello world!'), ['Hello', 'world!'])
        self.assertEqual(function_under_test('Hello,world!'), ['Hello', 'world!'])
        self.assertEqual(function_under_test('abcdef'), 3)

if __name__ == '__main__':
    unittest.main()