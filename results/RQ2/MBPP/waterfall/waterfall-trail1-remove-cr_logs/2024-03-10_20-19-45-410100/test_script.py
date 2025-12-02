def return_sum(dict):
    total = 0
    for key, value in dict.items():
        if isinstance(value, (int, float)):
            total += value
        else:
            raise ValueError("Input dictionary contains non-numeric values.")
    return total
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()