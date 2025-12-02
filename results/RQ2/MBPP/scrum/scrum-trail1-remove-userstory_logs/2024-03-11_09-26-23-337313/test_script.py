def number_ctr(input_string):
    count = 0
    for char in input_string:
        if char.isdigit():
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(number_ctr('program2bedone'), 1)

if __name__ == '__main__':
    unittest.main()