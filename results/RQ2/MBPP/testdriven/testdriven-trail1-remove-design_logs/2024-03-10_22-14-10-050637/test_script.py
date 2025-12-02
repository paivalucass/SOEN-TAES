def average_tuple(nums):
    result = [sum(tup) / len(tup) for tup in nums]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [30.5, 34.25, 27.0, 23.25])

if __name__ == '__main__':
    unittest.main()