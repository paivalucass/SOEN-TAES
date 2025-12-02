def capital_words_spaces(str1):
    result = []
    for char in str1:
        if char.isupper():
            result.append(' ')
        result.append(char)
    return ''.join(result).strip()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(capital_words_spaces('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()