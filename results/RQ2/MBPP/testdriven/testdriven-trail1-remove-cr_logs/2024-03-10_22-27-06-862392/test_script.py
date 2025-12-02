def find_Rotations(str):
    if len(set(str)) == 1:
        return 1
    return len(str)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Rotations('aaaa'), 1)

if __name__ == '__main__':
    unittest.main()