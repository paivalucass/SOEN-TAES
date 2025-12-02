def interleave_lists(list1, list2, list3):
    if len(list1) != len(list2) or len(list1) != len(list3) or len(list2) != len(list3) or len(list1) == 0 or len(list2) == 0 or len(list3) == 0:
        return "Error: Lists are of different lengths or empty"
    
    result = []
    for item1, item2, item3 in zip(list1, list2, list3):
        result.extend([item1, item2, item3])
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_interleave_lists(self):
        self.assertEqual(interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]), [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700])

if __name__ == '__main__':
    unittest.main()