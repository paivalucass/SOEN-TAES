def return_sum(input_dict):
    if not isinstance(input_dict, dict):
        raise TypeError("Input is not a dictionary")

    for value in input_dict.values():
        if not isinstance(value, (int, float)):
            raise ValueError("Non-numeric value found in the dictionary")

    return sum(input_dict.values())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()