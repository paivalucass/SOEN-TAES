def tuple_to_int(nums):
    if not isinstance(nums, tuple):
        raise ValueError("Input must be a tuple")
    if not all(isinstance(num, int) and num > 0 for num in nums):
        raise ValueError("All elements in the tuple must be positive integers")

    return int(''.join(map(str, nums)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_int((1,2,3)), 123)

if __name__ == '__main__':
    unittest.main()