def remove_odd(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]

    if not all(isinstance(num, int) for num in input_list):
        raise ValueError("Input list should only contain numbers")

    return even_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd([1,2,3]), [2])

if __name__ == '__main__':
    unittest.main()