def count_Substrings(s):
    if not s:
        return 0
    if not any(char.isdigit() for char in s):
        return 0

    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if sub.isdigit() and sum(int(digit) for digit in sub) == len(sub):
                count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Substrings('112112'), 6)

if __name__ == '__main__':
    unittest.main()