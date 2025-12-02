def Split(nums):
    if not isinstance(nums, list):
        raise TypeError("Input is not a list")

    if not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("Input list contains non-numeric values")

    even_numbers = [x for x in nums if x % 2 == 0]
    return even_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5]), [2,4])

if __name__ == '__main__':
    unittest.main()