def second_smallest(numbers):
    min_num = min(numbers)
    numbers = [num for num in numbers if num != min_num]
    second_min_num = min(numbers)
    return second_min_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(second_smallest([1, 2, -8, -2, 0, -2]), -2)

if __name__ == '__main__':
    unittest.main()