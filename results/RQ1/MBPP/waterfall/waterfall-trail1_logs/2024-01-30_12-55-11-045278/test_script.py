def dict_filter(input_dict: dict, n: int) -> dict:
    if not isinstance(input_dict, dict) or len(input_dict) == 0:
        raise ValueError("Input dictionary is empty or not a valid dictionary")
    if not isinstance(n, int):
        raise ValueError("Input value n is not a valid integer")

    filtered_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, (int, float)) and value >= n:
            filtered_dict[key] = value

    return filtered_dict
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170), {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190})

if __name__ == '__main__':
    unittest.main()