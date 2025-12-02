def is_undulating(n):
    n_str = str(n)
    if len(n_str) < 3:
        return False
    for i in range(2, len(n_str)):
        if n_str[i] == n_str[i-2]:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_undulating(1212121), True)

if __name__ == '__main__':
    unittest.main()