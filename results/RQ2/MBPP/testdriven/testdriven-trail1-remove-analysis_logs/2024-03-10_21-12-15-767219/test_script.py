def find_even_pair(A):
    freq_set = set()
    count = 0
    
    for num in A:
        freq_set.add(num)
    
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            xor_result = A[i] ^ A[j]
            if xor_result % 2 == 0:
                count += 1
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_even_pair([5, 4, 7, 2, 1]), 4)

if __name__ == '__main__':
    unittest.main()