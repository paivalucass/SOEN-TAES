def count(lst):
    if not isinstance(lst, list):
        raise TypeError("Input should be a list")
    
    for item in lst:
        if not isinstance(item, bool):
            raise ValueError("List should contain only boolean values")

    true_count = lst.count(True)
    
    return true_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count([True, False, True]), 2)

if __name__ == '__main__':
    unittest.main()