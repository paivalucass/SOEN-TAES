def find_even_pair(A):
    count = 0
    xor_count = {}
    for num in A:
        if num in xor_count:
            count += xor_count[num]
        xor_count[num ^ 1] = xor_count.get(num ^ 1, 0) + 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_even_pair([5, 4, 7, 2, 1]), 4)

if __name__ == '__main__':
    unittest.main()