def find_even_pair(A):
    even_count = sum(1 for num in A if num % 2 == 0)
    odd_count = len(A) - even_count
    
    pair_count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (A[i] ^ A[j]) % 2 == 0:
                pair_count += 1
    return pair_count

assert find_even_pair([5, 4, 7, 2, 1]) == 4
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_even_pair([5, 4, 7, 2, 1]), 4)

if __name__ == '__main__':
    unittest.main()