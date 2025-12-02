def find_even_pair(A):
    '''Write a function that counts the number of pairs of integers in a list that xor to an even number.
    
    Args:
    A (list): Input list of integers
    
    Returns:
    int: Number of pairs of integers in the list that xor to an even number
    '''

    xor_even_count = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if (A[i] ^ A[j]) % 2 == 0:
                xor_even_count += 1
    return xor_even_count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_even_pair([5, 4, 7, 2, 1]), 4)

if __name__ == '__main__':
    unittest.main()