def any_int(first_num, second_num, third_num):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True

    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True

    any_int(3.6, -2.2, 2) ➞ False
    '''
    if isinstance(first_num, int) and isinstance(second_num, int) and isinstance(third_num, int):
        return (first_num == second_num + third_num) or (second_num == first_num + third_num) or (third_num == first_num + second_num)
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(any_int(5, 2, 7), True)
        self.assertEqual(any_int(3, 2, 2), False)
        self.assertEqual(any_int(3, -2, 1), True)
        self.assertEqual(any_int(3.6, -2.2, 2), False)

if __name__ == '__main__':
    unittest.main()