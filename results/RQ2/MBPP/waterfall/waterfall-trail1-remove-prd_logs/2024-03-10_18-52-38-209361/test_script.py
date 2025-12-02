def rev(num):
    try:
        num = int(num)
    except ValueError:
        return "Error: Input is not a valid integer"
    reversed_num = int(str(num)[::-1])
    if num == 2 * reversed_num - 1:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check(70), False)

if __name__ == '__main__':
    unittest.main()