def check(num):
    reverse_num = int(str(num)[::-1])
    if num == reverse_num * 2 - 1:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check(70), False)

if __name__ == '__main__':
    unittest.main()