def split(input_list):
    if not isinstance(input_list, list):
        raise TypeError("input_list must be a list")

    for num in input_list:
        if not isinstance(num, int):
            raise ValueError("All elements in input_list must be integers")

    odd_integers = [num for num in input_list if num % 2 != 0]
    return odd_integers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split([1,2,3,4,5,6]), [1,3,5])

if __name__ == '__main__':
    unittest.main()