def check_value(dictionary, value):
    if not dictionary:
        return False
    if value not in dictionary.values():
        return False
    return all(val == value for val in dictionary.values())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10), False)

if __name__ == '__main__':
    unittest.main()