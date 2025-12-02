def interleave_lists(list1, list2, list3):
    '''Write a function to interleave 3 lists of the same length into a single flat list.'''
    assert len(list1) == len(list2) == len(list3), "Input lists must be of the same length"
    
    if not list1 or not list2 or not list3:
        raise ValueError("Input lists cannot be empty")
    
    interleaved_list = [elem for sublist in zip(list1, list2, list3) for elem in sublist]
    
    return interleaved_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]), [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700])

if __name__ == '__main__':
    unittest.main()