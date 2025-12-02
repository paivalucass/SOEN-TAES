def Diff(li1,li2):
    difference_list = []
    
    if not isinstance(li1, list) or not isinstance(li2, list) or not li1 or not li2:
        raise ValueError("Invalid input parameters. Both input parameters should be non-empty lists.")
    
    for element in li1:
        if element not in li2:
            difference_list.append(element)
    
    return difference_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]), [10, 15, 20, 30])

if __name__ == '__main__':
    unittest.main()