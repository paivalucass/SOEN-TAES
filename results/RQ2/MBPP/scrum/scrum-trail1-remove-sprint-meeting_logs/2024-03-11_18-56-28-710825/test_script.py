def min_Swaps(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count / 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Swaps("1101", "1110"), 1)

if __name__ == '__main__':
    unittest.main()