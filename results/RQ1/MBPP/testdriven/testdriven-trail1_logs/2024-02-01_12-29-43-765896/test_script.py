def get_Inv_Count(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                result += 1
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Inv_Count([1, 20, 6, 4, 5]), 5)

if __name__ == '__main__':
    unittest.main()