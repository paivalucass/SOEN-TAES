def is_special_number(num):
    def reverse_num(n):
        return int(str(n)[::-1])
    if num == (2 * reverse_num(num) + 1):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check(70), False)

if __name__ == '__main__':
    unittest.main()