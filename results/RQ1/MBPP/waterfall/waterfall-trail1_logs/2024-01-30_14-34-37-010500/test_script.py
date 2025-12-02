def check_value(input_dict, expected_value):
    unique_values = set(input_dict.values())
    return len(unique_values) == 1 and list(unique_values)[0] == expected_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertFalse(check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10))

if __name__ == '__main__':
    unittest.main()