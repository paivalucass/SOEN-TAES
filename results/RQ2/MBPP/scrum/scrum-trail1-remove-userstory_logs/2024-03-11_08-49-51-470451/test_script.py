def find_Rotations(input_string):
    if len(set(input_string)) == 1:
        return 1
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()