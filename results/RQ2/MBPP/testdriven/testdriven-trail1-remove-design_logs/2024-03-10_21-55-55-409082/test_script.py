def smallest_num(xs):
    '''
    Write a python function to find smallest number in a list.
    assert smallest_num([10, 20, 1, 45, 99]) == 1
    '''

    if not isinstance(xs, list):
        return "Invalid Input"
    elif not xs:
        return None
    else:
        try:
            return min(xs)
        except TypeError:
            return "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

if __name__ == '__main__':
    unittest.main()