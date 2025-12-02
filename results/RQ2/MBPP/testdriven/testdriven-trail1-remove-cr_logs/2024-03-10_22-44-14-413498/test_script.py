def find_Odd_Pair(A, N):
    if not A or N <= 0:
        return "Invalid input: Array is empty or length is not valid"
    
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i] ^ A[j]) % 2 != 0:
                count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Odd_Pair([5,4,7,2,1], 5), 6)

if __name__ == '__main__':
    unittest.main()