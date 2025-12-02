def dict_filter(dictionary, n):
    if not isinstance(dictionary, dict):
        raise TypeError("Input must be a dictionary")
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    filtered_dict = {key: value for key, value in dictionary.items() if value >= n}
    return filtered_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}, 170), {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190})

if __name__ == '__main__':
    unittest.main()