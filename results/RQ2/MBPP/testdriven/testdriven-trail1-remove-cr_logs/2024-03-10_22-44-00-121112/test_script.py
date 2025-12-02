def remove_lowercase(str1):
    modified_string = ''
    for char in str1:
        if not char.islower():
            modified_string += char
    return modified_string.strip()
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_lowercase('PYTHon'), 'PYTH')

if __name__ == '__main__':
    unittest.main()