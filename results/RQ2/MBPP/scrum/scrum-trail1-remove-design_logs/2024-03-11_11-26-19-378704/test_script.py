def Split(input_list):
    odd_integers = [num for num in input_list if num % 2 != 0]
    return odd_integers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5,6]), [1,3,5])

if __name__ == '__main__':
    unittest.main()