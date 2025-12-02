def find_Odd_Pair(A, N):
    memo = {}
    count = 0
    
    for i in range(N):
        for j in range(i+1, N):
            xor_val = A[i] ^ A[j]
            if xor_val % 2 != 0:
                count += 1
            memo[(i, j)] = xor_val

    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Odd_Pair([5,4,7,2,1],5), 6)

if __name__ == '__main__':
    unittest.main()