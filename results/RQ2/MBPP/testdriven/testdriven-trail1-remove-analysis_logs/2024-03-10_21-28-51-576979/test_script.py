def unique_Element(arr):
    distinct_elements = set(arr)
    if len(distinct_elements) == 1:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_Element([1,1,1]), True)

if __name__ == '__main__':
    unittest.main()