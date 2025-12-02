def flatten_list(input_list):
    result = []
    for item in input_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            if isinstance(item, (int, float)):
                result.append(item)
            else:
                return 'Error: Non-numeric elements present'
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]), 
                         [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

if __name__ == '__main__':
    unittest.main()