def is_Sub_Array(A, B):
    m = len(A)
    n = len(B)

    if n == 0:
        return True

    if n > m:
        return False

    lps = [0] * n
    j = 0

    compute_lps_array(B, n, lps)

    i = 0
    while i < m:
        if B[j] == A[i]:
            i += 1
            j += 1

            if j == n:
                return True
            j = lps[j-1]
        elif i < m and B[j] != A[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    return False

def compute_lps_array(B, n, lps):
    length = 0
    lps[0] = 0
    i = 1

    while i < n:
        if B[i] == B[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sub_Array([1,4,3,5],[1,2]), False)

if __name__ == '__main__':
    unittest.main()