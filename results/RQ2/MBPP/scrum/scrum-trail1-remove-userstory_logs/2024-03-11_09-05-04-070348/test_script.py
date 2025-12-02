def dict_filter(input_dict, n):
    '''Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
    assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}'''
    if not isinstance(input_dict, dict):
        raise TypeError("Input must be a dictionary type")
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    filtered_dict = {key: value for key, value in input_dict.items() if value >= n}
    return filtered_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170), {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190})

if __name__ == '__main__':
    unittest.main()