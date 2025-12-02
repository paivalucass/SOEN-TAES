def find_Odd_Pair(A, N):
    count = 0
    odd_count = 0
    even_count = 0
    for num in A:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    count = odd_count * even_count
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Odd_Pair([5,4,7,2,1], 5), 6)

if __name__ == '__main__':
    unittest.main()