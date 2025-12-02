def swap_List(input_list):
    if not isinstance(input_list, list) or len(input_list) < 1:
        return "Input list is empty or not valid. Please provide a valid list."

    new_list = input_list[:]
    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_List([12, 35, 9, 56, 24]), [24, 35, 9, 56, 12])

if __name__ == '__main__':
    unittest.main()