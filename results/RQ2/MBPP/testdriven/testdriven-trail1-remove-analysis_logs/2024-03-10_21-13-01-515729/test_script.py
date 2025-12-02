def larg_nnum(list1, n):
    '''Write a function that takes in a list and an integer n and returns a list containing the n largest items from the list.'''
    import heapq
    if not list1:
        return "Input list is empty"
    elif n > len(list1):
        return "n is greater than the length of the input list"
    
    return heapq.nlargest(n, list1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2), [100, 90])

if __name__ == '__main__':
    unittest.main()