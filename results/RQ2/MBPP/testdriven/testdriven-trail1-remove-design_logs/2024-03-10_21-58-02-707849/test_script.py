def count(lst):
    true_count = 0
    for item in lst:
        if isinstance(item, bool):
            if item == True:
                true_count += 1
    return true_count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count([True,False,True]), 2)

if __name__ == '__main__':
    unittest.main()