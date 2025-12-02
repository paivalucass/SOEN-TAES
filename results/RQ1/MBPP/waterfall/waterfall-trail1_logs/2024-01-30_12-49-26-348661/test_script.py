def count_integer(list1):
    count = sum(isinstance(element, int) for element in list1)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_integer([1,2,'abc',1.2]), 2)

if __name__ == '__main__':
    unittest.main()