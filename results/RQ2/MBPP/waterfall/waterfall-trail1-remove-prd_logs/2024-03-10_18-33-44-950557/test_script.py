def dict_filter(input_dict, threshold_value):
    if not isinstance(input_dict, dict) or not isinstance(threshold_value, int):
        raise ValueError("Input dictionary is empty or threshold_value is not a valid integer")

    return {key: value for key, value in input_dict.items() if value >= threshold_value}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170), {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190})

if __name__ == '__main__':
    unittest.main()