def is_undulating(n):
    if len(str(n)) < 3:
        return False
    n_str = str(n)
    increasing = n_str[0] < n_str[1]
    for i in range(1, len(n_str) - 1):
        if (n_str[i] < n_str[i+1]) == increasing:
            return False
        increasing = not increasing
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_undulating(1212121), True)

if __name__ == '__main__':
    unittest.main()