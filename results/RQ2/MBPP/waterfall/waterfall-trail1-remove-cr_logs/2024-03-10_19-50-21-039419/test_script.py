def rev(num):
    if not isinstance(num, int) or num <= 0:
        return False
    reverse_num = int(str(num)[::-1])
    return num == (2 * reverse_num) - 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check(70), False)

if __name__ == '__main__':
    unittest.main()