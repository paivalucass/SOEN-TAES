def second_smallest(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(second_smallest([1, 2, -8, -2, 0, -2]), -2)

if __name__ == '__main__':
    unittest.main()