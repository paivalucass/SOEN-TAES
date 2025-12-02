def check(num):
    if not isinstance(num, int):
        return "Error: Input must be an integer"
    if num < 0 or num > 100:
        return "Error: Input must be within the range of 0 to 100"
    
    def rev(num):
        return int(str(num)[::-1])
    
    return num == 2*rev(num) - 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check(70), False)

if __name__ == '__main__':
    unittest.main()