def find_Odd_Pair(A, N):
    oddCount = sum(1 for num in A if num % 2 != 0)
    evenCount = N - oddCount
    result = oddCount * evenCount
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Odd_Pair([5, 4, 7, 2, 1], 5), 6)

if __name__ == '__main__':
    unittest.main()