def second_smallest(numbers):
    if len(numbers) < 2:
        return "List should have at least two different numbers"
    else:
        unique_numbers = list(set(numbers))
        min_num = min(unique_numbers)
        unique_numbers.remove(min_num)
        second_min = min(unique_numbers)
        return second_min
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(second_smallest([1, 2, -8, -2, 0, -2]), -2)

if __name__ == '__main__':
    unittest.main()