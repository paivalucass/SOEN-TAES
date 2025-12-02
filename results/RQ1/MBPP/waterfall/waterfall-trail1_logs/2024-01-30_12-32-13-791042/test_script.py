def tuple_to_int(nums):
    if not isinstance(nums, tuple):
        raise TypeError("Input is not a tuple")
    
    if len(nums) == 0:
        raise ValueError("Input tuple is empty")

    for num in nums:
        if not isinstance(num, int) or num < 0:
            raise ValueError("Input tuple contains non-positive integers")

    result = int(''.join(map(str, nums)))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

if __name__ == '__main__':
    unittest.main()