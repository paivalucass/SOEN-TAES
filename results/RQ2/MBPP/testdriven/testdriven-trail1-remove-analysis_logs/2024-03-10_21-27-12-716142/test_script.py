def sum_list(lst1, lst2):
    '''
    Write a function that takes as input two lists [a_1,...,a_n], [b_1,...,b_n] and returns [a_1+b_1,...,a_n+b_n].
    assert sum_list([10,20,30],[15,25,35])==[25,45,65]
    '''

    # Ensure both input lists are of the same length
    if len(lst1) != len(lst2):
        raise ValueError("Input lists must be of the same length")

    # Sum elements of lst1 and lst2 and store the result in a new list
    result = [x + y for x, y in zip(lst1, lst2)]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_list([10,20,30], [15,25,35]), [25,45,65])

if __name__ == '__main__':
    unittest.main()