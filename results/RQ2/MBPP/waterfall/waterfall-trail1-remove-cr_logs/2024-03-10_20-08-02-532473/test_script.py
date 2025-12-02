def remove_lowercase(str1):
    result = ""

    if str1 is None or str1 == "":
        return ""

    for char in str1:
        if char.isupper():
            result += char

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_lowercase('PYTHon'), 'PYTH')

if __name__ == '__main__':
    unittest.main()