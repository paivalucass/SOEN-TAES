def count_Substrings(s):
    if not s:
        return 0
    for char in s:
        if not char.isdigit():
            return "Invalid Input"
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if sum(int(x) for x in sub) == len(sub):
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_Substrings(self):
        self.assertEqual(count_Substrings('112112'), 6)

if __name__ == '__main__':
    unittest.main()