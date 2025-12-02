def return_sum(dictionary):
    if not isinstance(dictionary, dict):
        return "Error: Invalid input"
    total_sum = sum(value for value in dictionary.values() if isinstance(value, (int, float)))
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()