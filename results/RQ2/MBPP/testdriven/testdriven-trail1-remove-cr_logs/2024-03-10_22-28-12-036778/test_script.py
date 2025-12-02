def max_difference(test_list):
    if test_list is None:
        return "Error: Null input data"
    if len(test_list) == 0:
        return "Error: Empty input list"

    num_elements = len(test_list[0])
    for tpl in test_list:
        if len(tpl) != num_elements:
            return "Error: Tuples have different number of elements"

    max_diff = 0
    for tpl in test_list:
        for i in range(len(tpl)-1):
            if not (isinstance(tpl[i], (int, float)) and isinstance(tpl[i+1], (int, float))):
                return "Error: Invalid input data"
            diff = abs(tpl[i] - tpl[i+1])
            if diff > max_diff:
                max_diff = diff
    
    return max_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]), 7)

if __name__ == '__main__':
    unittest.main()