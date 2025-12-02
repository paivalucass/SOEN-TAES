def split_number_list(number_list):
    even_numbers = []
    for number in number_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5]), [2,4])

if __name__ == '__main__':
    unittest.main()