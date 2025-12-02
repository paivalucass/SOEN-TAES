def check_value(input_dict, input_value):
    if not input_dict or input_value not in input_dict.values():
        return False
    return all(value == input_value for value in input_dict.values())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10), False)

if __name__ == '__main__':
    unittest.main()