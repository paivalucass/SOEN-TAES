def will_it_fly(q, w):
    '''
    Check if the object_list will fly, return True if it's balanced and the sum of its elements is less than or equal to the maximum possible weight.

    Args:
    q (list): A list of integers representing the weights of the objects.
    w (int): The maximum possible weight.

    Returns:
    bool: True if the object_list will fly, False otherwise.

    '''
    if not isinstance(q, list) or not all(isinstance(i, int) for i in q):
        raise ValueError('q must be a list of integers')
        
    if not isinstance(w, int) or w <= 0:
        raise ValueError('w must be a positive integer')
    
    if q != q[::-1]:
        return False

    if sum(q) <= w:
        return True

    return False
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(will_it_fly([1, 2], 5), False)
    
    def test2(self):
        self.assertEqual(will_it_fly([3, 2, 3], 1), False)
    
    def test3(self):
        self.assertEqual(will_it_fly([3, 2, 3], 9), True)
    
    def test4(self):
        self.assertEqual(will_it_fly([3], 5), True)

if __name__ == '__main__':
    unittest.main()