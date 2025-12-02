def average_tuple(nums):
    averages = []
    for tpl in nums:
        avg = sum(tpl) / len(tpl)
        averages.append(round(avg, 2))
    return averages
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [30.5, 34.25, 33.0, 2.5])

if __name__ == '__main__':
    unittest.main()