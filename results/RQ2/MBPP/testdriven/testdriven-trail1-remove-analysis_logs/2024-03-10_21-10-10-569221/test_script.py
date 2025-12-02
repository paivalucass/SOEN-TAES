def count(lst):
    true_count = lst.count(True)
    return true_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count([True,False,True]), 2)

if __name__ == '__main__':
    unittest.main()