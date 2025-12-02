def return_sum(dictionary):
    try:
        if not dictionary:
            return 0
        total = 0
        for key, value in dictionary.items():
            if not isinstance(value, (int, float)):
                raise ValueError("Non-numeric value in the dictionary")
            total += value
        return total
    except (ValueError, TypeError):
        return "Error: Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()