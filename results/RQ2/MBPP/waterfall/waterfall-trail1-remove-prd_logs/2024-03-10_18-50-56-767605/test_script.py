def is_special_number(num):
    try:
        num = int(num)
    except ValueError:
        return False

    reverse_num = int(str(num)[::-1])
    if num == 2 * reverse_num - 1:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check(70), False)

if __name__ == '__main__':
    unittest.main()