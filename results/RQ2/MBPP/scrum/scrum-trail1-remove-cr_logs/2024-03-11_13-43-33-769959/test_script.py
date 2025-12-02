def min_Swaps(str1, str2):
    count = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Swaps("1101", "1110"), 1)

if __name__ == '__main__':
    unittest.main()