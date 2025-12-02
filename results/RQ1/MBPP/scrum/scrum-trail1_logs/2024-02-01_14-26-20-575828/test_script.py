def is_undulating(n):
    # Function to check whether the given number is undulating or not
    n_str = str(n)
    if len(n_str) < 3:
        return False
    for i in range(0, len(n_str)-2, 2):
        if n_str[i] == n_str[i+1] or n_str[i+1] == n_str[i+2]:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_undulating(1212121), True)

if __name__ == '__main__':
    unittest.main()