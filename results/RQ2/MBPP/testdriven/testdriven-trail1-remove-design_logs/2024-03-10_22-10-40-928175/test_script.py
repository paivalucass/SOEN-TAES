def remove_lowercase(str1):
    result = ''.join(char for char in str1 if not char.islower())
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_lowercase('PYTHon'), 'PYTH')

if __name__ == '__main__':
    unittest.main()