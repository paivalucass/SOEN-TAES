def odd_Equivalent(s, n):
    if s == "" or n == 0:
        return 0
    else:
        s = s * 2
        rotated_string = s[n % len(s):n % len(s) + len(s)]
        count_odd = 0
        for char in rotated_string:
            if int(char) % 2 != 0:
                count_odd += 1
        return count_odd
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()