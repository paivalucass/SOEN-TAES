def find_even_pair(A):
    count = 0
    num_count = {"even": 0, "odd": 0}
    for num in A:
        if num % 2 == 0:
            num_count["even"] += 1
        else:
            num_count["odd"] += 1
    
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