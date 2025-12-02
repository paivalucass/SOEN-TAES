def sum_even_and_even_index(arr):
    if len(arr) == 0 or len(arr) % 2 != 0:
        return 0
    else:
        return sum(arr[i] for i in range(len(arr)) if arr[i] % 2 == 0 and i % 2 == 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_even_and_even_index([5, 6, 12, 1, 18, 8]), 30)

if __name__ == '__main__':
    unittest.main()