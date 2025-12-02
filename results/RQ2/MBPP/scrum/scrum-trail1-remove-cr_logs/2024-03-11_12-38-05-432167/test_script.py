def is_undulating(n):
    num_str = str(n)
    if len(num_str) < 3:
        return False
    if len(set(num_str)) != 2:
        return False
    if num_str[0] == num_str[1]:
        return False
    for i in range(2, len(num_str)):
        if i % 2 == 0:
            if num_str[i] != num_str[0]:
                return False
        else:
            if num_str[i] != num_str[1]:
                return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_undulating(1212121), True)

if __name__ == '__main__':
    unittest.main()