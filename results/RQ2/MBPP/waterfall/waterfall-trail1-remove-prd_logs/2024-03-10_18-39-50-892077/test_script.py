def upper_ctr(input_string):
    count = 0
    for char in input_string:
        if char.isupper():
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(upper_ctr('PYthon'), 2)

if __name__ == '__main__':
    unittest.main()