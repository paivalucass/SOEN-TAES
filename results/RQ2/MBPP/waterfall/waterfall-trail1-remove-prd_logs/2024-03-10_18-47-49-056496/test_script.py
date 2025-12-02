def unique_Element(arr):
    if len(arr) == 0:
        return False
    return len(set(arr)) == 1

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_Element([1,1,1]), True)

if __name__ == '__main__':
    unittest.main()