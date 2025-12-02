def sequential_search(dlist, item):
    '''Write a function that takes in an array and element and returns a tuple containing a boolean that indicates if the element is in the array and the index position of the element (or -1 if the element is not found).'''
    if len(dlist) == 0:
        return "Error: Input array is empty"
    if not item:
        return "Error: Input element is empty"
    
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)
    
    return (False, -1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequential_search([11,23,58,31,56,77,43,12,65,19],31), (True, 3))

if __name__ == '__main__':
    unittest.main()