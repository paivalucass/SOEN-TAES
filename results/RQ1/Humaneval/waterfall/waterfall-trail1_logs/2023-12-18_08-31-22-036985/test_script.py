def sum_squares(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    
    if not all(isinstance(num, int) for num in lst):
        raise ValueError("List must contain only integers")
    
    result = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            result += lst[i] ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += lst[i] ** 3
    
    return result
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(sum_squares([1,2,3]), 6)
        
    def test2(self):
        self.assertEqual(sum_squares([]), 0)
        
    def test3(self):
        self.assertEqual(sum_squares([-1,-5,2,-1,-5]), -126)

if __name__ == '__main__':
    unittest.main()