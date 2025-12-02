def upper_ctr(input_string, case_insensitive=False):
    count = 0
    if case_insensitive:
        input_string = input_string.lower()
    for char in input_string:
        if char.isupper():
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_upper_ctr(self):
        self.assertEqual(upper_ctr('PYthon'), 2)

if __name__ == '__main__':
    unittest.main()