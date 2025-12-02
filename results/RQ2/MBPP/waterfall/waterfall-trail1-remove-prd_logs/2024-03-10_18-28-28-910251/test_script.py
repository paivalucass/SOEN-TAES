def count(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    for item in lst:
        if not isinstance(item, bool):
            raise ValueError("List must contain only boolean values")
    
    return lst.count(True)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count([True,False,True]), 2)

if __name__ == '__main__':
    unittest.main()