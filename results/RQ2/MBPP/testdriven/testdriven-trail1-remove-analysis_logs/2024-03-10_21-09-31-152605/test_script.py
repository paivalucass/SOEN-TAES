def is_undulating(n):
    num_str = str(n)
    if len(num_str) < 3:
        return False
    increasing = True
    for i in range(2, len(num_str)):
        if (increasing and num_str[i] <= num_str[i-1] <= num_str[i-2]) or (not increasing and num_str[i] >= num_str[i-1] >= num_str[i-2]):
            increasing = not increasing
        else:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_undulating(1212121), True)

if __name__ == '__main__':
    unittest.main()