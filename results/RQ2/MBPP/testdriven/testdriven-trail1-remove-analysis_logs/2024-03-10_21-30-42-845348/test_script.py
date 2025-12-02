def return_sum(input_dict):
    sum = 0
    for key, value in input_dict.items():
        if isinstance(value, (int, float)):
            sum += value
        else:
            return "Invalid input data type"
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()