def return_sum(input_dict: dict) -> int:
    if not isinstance(input_dict, dict):
        raise TypeError("Input must be a dictionary")
    
    sum = 0
    for key in input_dict:
        if not isinstance(input_dict[key], (int, float)):
            raise ValueError("Dictionary values must be numeric")
        sum += input_dict[key]
    
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()