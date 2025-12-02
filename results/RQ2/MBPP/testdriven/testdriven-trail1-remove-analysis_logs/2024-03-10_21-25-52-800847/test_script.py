def split(numbers_list):
    even_numbers = [number for number in numbers_list if isinstance(number, int) and number % 2 == 0]
    return even_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5]), [2,4])

if __name__ == '__main__':
    unittest.main()