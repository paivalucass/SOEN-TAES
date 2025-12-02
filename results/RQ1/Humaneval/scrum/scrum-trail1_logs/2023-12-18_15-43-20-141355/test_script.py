def add_elements(arr, k):
    return sum(x for x in arr[:k] if 10 <= x <= 99)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_elements([111,21,3,4000,5,6,7,8,9], 4), 24)

if __name__ == '__main__':
    unittest.main()