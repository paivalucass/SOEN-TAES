def find_odd_pair(A, N):
  odd_count = 0
  for i in range(N):
    for j in range(i+1, N):
      if bin(A[i] ^ A[j]).count('1') % 2 != 0:
        odd_count += 1
  return odd_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Odd_Pair([5,4,7,2,1], 5), 6)

if __name__ == '__main__':
    unittest.main()