def count(lst):
    if not all(isinstance(item, bool) for item in lst):
        raise ValueError("Input list should only contain boolean values")

    return lst.count(True)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count([True,False,True]), 2)

if __name__ == '__main__':
    unittest.main()