def remove_lowercase(str1):
    if not isinstance(str1, str):
        raise TypeError("Input must be a string")
    
    return ''.join(filter(lambda x: x.isupper(), str1))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_lowercase('PYTHon'), 'PYTH')

if __name__ == '__main__':
    unittest.main()