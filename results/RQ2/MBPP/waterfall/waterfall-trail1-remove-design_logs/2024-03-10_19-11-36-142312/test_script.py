def dict_filter(dictionary, n):
    if not isinstance(dictionary, dict) or not isinstance(n, (int, float)):
        raise ValueError("Input validation failed: 'dictionary' should be a dictionary and 'n' should be a number.")

    filtered_dict = {key: val for key, val in dictionary.items() if val >= n}
    return filtered_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170), {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190})

if __name__ == '__main__':
    unittest.main()