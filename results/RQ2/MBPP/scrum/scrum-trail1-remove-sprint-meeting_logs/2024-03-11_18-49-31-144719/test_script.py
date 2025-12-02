def check_value(dict, n):
    values = list(dict.values())
    return all(value == values[0] for value in values)
import unittest

class Test(unittest.TestCase):
    def test_check_value(self):
        self.assertEqual(check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10), True)

if __name__ == '__main__':
    unittest.main()