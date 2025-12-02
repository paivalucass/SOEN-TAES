def average_tuple(nums):
    result = []
    for t in nums:
        if len(t) == 0:
            result.append(None)
        else:
            result.append(round(sum(t) / len(t), 2))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [30.5, 34.25, 33.0, 2.5])

if __name__ == '__main__':
    unittest.main()