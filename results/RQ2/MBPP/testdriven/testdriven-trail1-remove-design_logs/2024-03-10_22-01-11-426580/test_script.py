def re_arrange_array(arr, n):
    '''
    Write a function that takes in an array and an integer n, and re-arranges the first n elements of the given array so that all negative elements appear before positive ones, and where the relative order among negative and positive elements is preserved.
    '''
    
    negative_numbers = [i for i in arr if i < 0]
    positive_numbers = [i for i in arr if i >= 0]
    
    return negative_numbers + [i for i in positive_numbers if i not in negative_numbers][:n - len(negative_numbers)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9), [-1, -3, -7, 4, 5, 6, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()