def dict_filter(input_dict, n):
    if not isinstance(input_dict, dict) or not isinstance(n, int):
        raise ValueError('Input is not a dictionary or n is not a valid number')
    
    filtered_dict = {key: value for key, value in input_dict.items() if value >= n}
    return filtered_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170), 
                         {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190})

if __name__ == '__main__':
    unittest.main()