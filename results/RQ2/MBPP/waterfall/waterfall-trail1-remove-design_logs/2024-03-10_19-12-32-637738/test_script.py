def get_Inv_Count(arr):
    n = len(arr)
    inv_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Inv_Count([1, 20, 6, 4, 5]), 5)

if __name__ == '__main__':
    unittest.main()