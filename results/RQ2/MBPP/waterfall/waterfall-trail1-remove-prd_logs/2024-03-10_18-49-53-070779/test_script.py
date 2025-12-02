def return_sum(dictionary):
    if not isinstance(dictionary, dict):
        raise TypeError("Input must be a dictionary")

    if not all(isinstance(value, (int, float)) for value in dictionary.values()):
        raise ValueError("All values in the dictionary must be numeric")

    if len(dictionary) == 0:
        return 0

    total_sum = sum(dictionary.values())
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()