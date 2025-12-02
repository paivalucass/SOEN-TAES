def number_ctr(str):
    count = 0
    for char in str:
        if char.isdigit():
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_number_ctr(self):
        self.assertEqual(number_ctr('program2bedone'), 1)

if __name__ == '__main__':
    unittest.main()