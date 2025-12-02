def remove_odd(list_of_numbers):
    """
    This function removes odd numbers from the given list and returns a new list with only even numbers.
    """
    return [x for x in list_of_numbers if x % 2 == 0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd([1,2,3]), [2])

if __name__ == '__main__':
    unittest.main()