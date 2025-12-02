def find_Index(n):
    '''Write a python function to find the index of smallest triangular number with n digits. https://www.geeksforgeeks.org/index-of-smallest-triangular-number-with-n-digits/'''
    
    if n == 1:
        return 1
    elif n == 2:
        return 4
    else:
        index = 1
        triangular_num = 3
        while len(str(triangular_num)) < n:
            index += 1
            triangular_num = (index * (index + 1)) // 2
        return index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Index(2), 4)

if __name__ == '__main__':
    unittest.main()