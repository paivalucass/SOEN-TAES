def average_tuple(nums):
    if not nums:
        return "Invalid input"
    
    averages = []
    for tup in nums:
        if any(not isinstance(i, (int, float)) for i in tup):
            return "Invalid input"
        avg = sum(tup) / len(tup)
        averages.append(round(avg, 2))
    return averages
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))), [30.5, 34.25, 58.0, 2.5])

if __name__ == '__main__':
    unittest.main()