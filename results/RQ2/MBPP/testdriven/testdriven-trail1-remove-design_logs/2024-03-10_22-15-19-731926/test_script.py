def pair_xor_Sum(arr, n):
    xor_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            xor_sum += arr[i] ^ arr[j]
    return xor_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pair_xor_Sum([5,9,7,6],4), 47)

if __name__ == '__main__':
    unittest.main()