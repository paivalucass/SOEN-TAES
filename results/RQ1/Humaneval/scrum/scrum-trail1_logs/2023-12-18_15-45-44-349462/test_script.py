def split_words(txt):
    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        odd_count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 != 0:
                odd_count += 1
        return odd_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test("Hello world!"), ["Hello", "world!"])
        self.assertEqual(function_under_test("Hello,world!"), ["Hello", "world!"])
        self.assertEqual(function_under_test("abcdef"), 3)

if __name__ == '__main__':
    unittest.main()