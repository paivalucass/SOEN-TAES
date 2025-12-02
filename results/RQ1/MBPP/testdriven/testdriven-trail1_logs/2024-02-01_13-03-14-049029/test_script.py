def min_Swaps(str1, str2):
    if len(str1) != len(str2):
        return "Error: Binary numbers are of different lengths"
    
    if not all(char in '01' for char in str1) or not all(char in '01' for char in str2):
        return "Error: Input strings should only contain 0s and 1s"

    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1

    return count // 2  # Since each swap will fix 2 differences
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_Swaps('1101', '1110'), 1)

if __name__ == '__main__':
    unittest.main()