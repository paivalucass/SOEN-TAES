def find_even_pair(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] ^ arr[j]) % 2 == 0:
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_even_pair([5, 4, 7, 2, 1]), 4)

if __name__ == '__main__':
    unittest.main()