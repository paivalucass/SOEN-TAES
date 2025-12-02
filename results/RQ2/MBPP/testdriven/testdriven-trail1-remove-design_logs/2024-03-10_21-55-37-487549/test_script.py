def rev(num):
    reverse_num = 0
    temp = num
    while temp > 0:
        remainder = temp % 10
        reverse_num = (reverse_num * 10) + remainder
        temp = temp // 10
    
    if num == ((reverse_num * 2) - 1):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check(70), False)

if __name__ == '__main__':
    unittest.main()