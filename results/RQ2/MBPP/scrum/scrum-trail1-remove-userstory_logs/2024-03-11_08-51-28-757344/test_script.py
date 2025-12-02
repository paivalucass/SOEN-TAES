def pos_count(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input should be a list of numbers")
    if len(numbers) == 0:
        return 0

    count = 0
    for num in numbers:
        if num > 0:
            count += 1

    return count
import unittest

class Test(unittest.TestCase):
    def test_pos_count(self):
        self.assertEqual(pos_count([1, -2, 3, -4]), 2)

if __name__ == '__main__':
    unittest.main()