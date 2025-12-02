def rev(num):
    if num < 0:
        return False
    
    if not isinstance(num, (int, float)):
        return False
    
    reversed_num = int(str(num)[::-1])
    
    return num == (2 * reversed_num - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check(70), False)

if __name__ == '__main__':
    unittest.main()