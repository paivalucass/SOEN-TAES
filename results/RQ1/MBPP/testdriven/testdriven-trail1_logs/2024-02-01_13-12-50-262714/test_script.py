def pair_xor_Sum(arr, n):
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            result += arr[i] ^ arr[j]
    return result
import unittest

class Test(unittest.TestCase):
    def test_pair_xor_Sum(self):
        self.assertEqual(pair_xor_Sum([5, 9, 7, 6], 4), 47)

if __name__ == '__main__':
    unittest.main()