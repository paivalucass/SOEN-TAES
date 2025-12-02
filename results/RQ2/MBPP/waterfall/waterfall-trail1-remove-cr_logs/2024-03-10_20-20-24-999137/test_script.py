def first_odd(nums):
    for num in nums:
        if isinstance(num, int):
            if num % 2 != 0:
                return num
        else:
            return "Invalid input"
    return "No odd number found"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(first_odd([1,3,5]), 1)

if __name__ == '__main__':
    unittest.main()