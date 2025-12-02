def remove_odd(input_list):
    return [num for num in input_list if num % 2 == 0]
import unittest

class Test(unittest.TestCase):
    def test_remove_odd(self):
        self.assertEqual(remove_odd([1,2,3]), [2])

if __name__ == '__main__':
    unittest.main()