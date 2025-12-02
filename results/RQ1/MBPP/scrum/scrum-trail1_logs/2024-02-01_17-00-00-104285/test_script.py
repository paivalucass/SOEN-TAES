def return_sum(data):
    if isinstance(data, dict):
        total_sum = 0
        for value in data.values():
            if isinstance(value, (int, float)):
                total_sum += value
            elif isinstance(value, dict):
                total_sum += return_sum(value)
            else:
                raise ValueError("Non-numeric value found in the dictionary")
        return total_sum
    else:
        raise TypeError("Input is not a dictionary")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()