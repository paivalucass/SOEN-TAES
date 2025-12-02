def validate(n):
    num_str = str(n)
    for i in range(1, 10):
        if num_str.count(str(i)) > i:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(validate(1234), True)

if __name__ == '__main__':
    unittest.main()