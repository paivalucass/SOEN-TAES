def cube_nums(nums):
    result = [round(num ** 3, 3) for num in nums]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])

if __name__ == '__main__':
    unittest.main()