def return_sum(dictionary):
    ''' 
    This function is designed to find the sum of all the numeric values in the given dictionary.

    Parameters:
    dictionary (dict): Input dictionary containing numeric values.

    Returns:
    int: The sum of all the numeric values in the input dictionary.

    Expected Behavior:
    - The input dictionary will always contain numeric values.
    - Validation for non-numeric values should be included.
    - If the input dictionary is empty, the function should return 0.
    '''

    if not isinstance(dictionary, dict):
        return "Invalid input"

    if not all(isinstance(value, (int, float)) for value in dictionary.values()):
        return "Invalid input"

    return sum(value for value in dictionary.values() if isinstance(value, (int, float)))

# Test cases
assert return_sum({}) == 0
assert return_sum({'a': 'apple', 'b': 'banana'}) == "Invalid input"
assert return_sum({'x': -100, 'y': 200, 'z': -300}) == -200
assert return_sum({'p': 10, 'q': '20', 'r': 30}) == "Invalid input"
assert return_sum({'m': 1000000000, 'n': 2000000000}) == 3000000000
assert return_sum({str(i): i for i in range(1000000)}) == 499999500000

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()