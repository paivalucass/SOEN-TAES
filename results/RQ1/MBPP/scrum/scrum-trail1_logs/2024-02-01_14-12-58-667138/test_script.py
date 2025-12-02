def check(num):
    reverse = int(str(num)[::-1])
    if num == (2 * reverse) - 1:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check(70), False)

if __name__ == '__main__':
    unittest.main()