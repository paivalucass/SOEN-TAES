def circular_shift(input_str, shift_amount):
    input_str_length = len(str(input_str))
    shift_amount = shift_amount % input_str_length
    
    if shift_amount == 0:
        return str(input_str)
    else:
        return str(input_str)[-shift_amount:] + str(input_str)[:-shift_amount]
import unittest

class Test(unittest.TestCase):
    def test_circular_shift(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(12, 2), "12")

if __name__ == '__main__':
    unittest.main()