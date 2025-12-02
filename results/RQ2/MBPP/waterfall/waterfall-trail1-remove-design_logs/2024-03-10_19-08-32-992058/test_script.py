def find_even_pair(A):
    count = 0
    even_count = 0
    odd_count = 0
    for num in A:
        if isinstance(num, int):
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    count = (even_count * (even_count - 1)) // 2 + (odd_count * (odd_count - 1)) // 2

    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_even_pair([5, 4, 7, 2, 1]), 4)

if __name__ == '__main__':
    unittest.main()