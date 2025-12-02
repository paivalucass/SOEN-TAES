def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub_string = s[i:j]
            if all(int(x) for x in sub_string) == len(sub_string):
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_Substrings(self):
        self.assertEqual(count_Substrings('112112'), 6)

if __name__ == '__main__':
    unittest.main()