def multiply_elements(test_tup):
    '''Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
    assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)'''
    
    if not isinstance(test_tup, tuple) or len(test_tup) == 0:
        return "Input is not a valid tuple or empty tuple"
    
    result = []
    for i in range(len(test_tup) - 1):
        result.append(test_tup[i] * test_tup[i+1])
    
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply_elements((1, 5, 7, 8, 10)), (5, 35, 56, 80))

if __name__ == '__main__':
    unittest.main()