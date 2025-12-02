def tuple_to_int(nums):
    if not nums:
        return 0
    for num in nums:
        if num <= 0:
            raise ValueError("Input tuple contains non-positive integers")
    result = int(''.join(map(str, nums)))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_int((1, 2, 3)), 123)

if __name__ == '__main__':
    unittest.main()