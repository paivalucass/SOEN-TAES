def lcs_of_three(X, Y, Z):
    # Initialize the lengths of the three strings
    m = len(X)
    n = len(Y)
    o = len(Z)
    
    # Initialize the 3D array to store the length of longest common subsequence
    L = [[[0 for i in range(o+1)] for j in range(n+1)] for k in range(m+1)]
    
    # Populate the 3D array using dynamic programming approach
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o+1):
                if i == 0 or j == 0 or k == 0:
                    L[i][j][k] = 0
                elif X[i-1] == Y[j-1] and X[i-1] == Z[k-1]:
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
                else:
                    L[i][j][k] = max(max(L[i-1][j][k], L[i][j-1][k]), L[i][j][k-1])
    
    # Return the length of longest common subsequence of the three strings
    return L[m][n][o]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lcs_of_three('AGGT12', '12TXAYB', '12XBA'), 2)

if __name__ == '__main__':
    unittest.main()