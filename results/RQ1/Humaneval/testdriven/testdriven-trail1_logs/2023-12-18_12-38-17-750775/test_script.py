def add_elements(arr, k):
    filtered_arr = [x for x in arr if -100 < x < 100]
    return sum(filtered_arr[:k])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([111,21,3,4000,5,6,7,8,9], 4), 24)

if __name__ == '__main__':
    unittest.main()