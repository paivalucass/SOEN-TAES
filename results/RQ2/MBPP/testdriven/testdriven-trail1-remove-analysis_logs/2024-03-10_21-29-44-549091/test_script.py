def find_sum(arr):
    total = 0
    for num in arr:
        if arr.count(num) == 1:
            total += num
    return total
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()