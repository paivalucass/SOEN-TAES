def remove_lowercase(input_string):
    result = ''.join([char for char in input_string if char.isupper()])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_lowercase('PYTHon'), 'PYTH')

if __name__ == '__main__':
    unittest.main()