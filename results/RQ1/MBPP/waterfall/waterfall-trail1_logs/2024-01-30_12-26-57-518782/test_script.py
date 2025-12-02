def is_undulating(n):
    num_str = str(n)
    for i in range(len(num_str) - 2):
        if (num_str[i] < num_str[i + 1] > num_str[i + 2]) or (num_str[i] > num_str[i + 1] < num_str[i + 2]):
            continue
        else:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_undulating(1212121), True)

if __name__ == '__main__':
    unittest.main()