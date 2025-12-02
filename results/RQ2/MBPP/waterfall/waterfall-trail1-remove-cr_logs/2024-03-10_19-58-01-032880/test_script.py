def count_integer(list1):
    if not isinstance(list1, list):
        raise ValueError("Input is not a list")

    integer_count = 0
    for element in list1:
        if isinstance(element, int):
            integer_count += 1

    return integer_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_integer([1,2,'abc',1.2]), 2)

if __name__ == '__main__':
    unittest.main()