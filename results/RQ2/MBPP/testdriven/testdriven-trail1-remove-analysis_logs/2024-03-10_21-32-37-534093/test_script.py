def find_even_numbers(input_list):
    even_numbers_list = []
    try:
        for num in input_list:
            if num % 2 == 0:
                even_numbers_list.append(num)
    except Exception as e:
        return "Invalid Input"
    return even_numbers_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5]), [2,4])

if __name__ == '__main__':
    unittest.main()