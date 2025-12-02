def find_sum(arr): 
    non_repeated_sum = sum(x for x in arr if arr.count(x) == 1)
    return non_repeated_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()