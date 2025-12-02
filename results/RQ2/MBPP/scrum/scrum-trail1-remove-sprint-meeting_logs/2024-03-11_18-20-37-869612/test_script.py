def odd_Equivalent(s, n):
    if not s:
        return 0
    
    if n < 0:
        return 0
    
    rotated_string = s[n % len(s):] + s[:n % len(s)]
    
    return sum(1 for char in rotated_string if int(char) % 2 != 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_Equivalent("011001", 6), 3)

if __name__ == '__main__':
    unittest.main()