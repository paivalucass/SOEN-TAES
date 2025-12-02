def check(num):
    return num == 2 * int(str(num)[::-1]) + 1

# Test cases
assert check(12) == True
assert check(25) == False
assert check(70) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check(70), False)

if __name__ == '__main__':
    unittest.main()