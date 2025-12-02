def find_even_pair(A):
    count = 0
    even_map = {0: 0, 1: 0}
    for num in A:
        if num % 2 == 0:
            count += even_map[0]
            even_map[0] += 1
        else:
            count += even_map[1]
            even_map[1] += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_even_pair([5, 4, 7, 2, 1]), 4)

if __name__ == '__main__':
    unittest.main()