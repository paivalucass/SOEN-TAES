def check_value(input_dict, comparison_value):
    if not input_dict or not all(isinstance(value, (int, float)) for value in input_dict.values()):
        raise ValueError("Input dictionary is empty or does not contain numeric values")
    
    return all(value == comparison_value for value in input_dict.values())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10), False)

if __name__ == '__main__':
    unittest.main()