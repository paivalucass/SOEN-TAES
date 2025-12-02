def tuple_to_int(nums):
    if not nums:
        raise ValueError("Input tuple cannot be empty")
    if any(num <= 0 for num in nums):
        raise ValueError("Input tuple must only contain positive integers")
    result = int(''.join(str(num) for num in nums))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tuple_to_int((1,2,3)), 123)

if __name__ == '__main__':
    unittest.main()