def find_even_pair(A):
    count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (A[i]^A[j]) % 2 == 0:
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_even_pair([5, 4, 7, 2, 1]), 4)

if __name__ == '__main__':
    unittest.main()