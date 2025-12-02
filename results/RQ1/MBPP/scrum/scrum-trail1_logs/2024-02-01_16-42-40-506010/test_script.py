def capital_words_spaces(str1):
    if str1 is None or len(str1) == 0:
        return ""

    result = ""
    for char in str1:
        if char.isupper():
            result += " " + char
        else:
            result += char

    return result.strip()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(capital_words_spaces('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()