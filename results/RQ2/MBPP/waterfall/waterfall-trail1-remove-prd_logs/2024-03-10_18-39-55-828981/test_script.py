def check_value(dictionary, n):
    return all(value == n for value in dictionary.values())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10), False)

if __name__ == '__main__':
    unittest.main()