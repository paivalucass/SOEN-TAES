def catalan_number(num):
    '''Write a function which returns nth catalan number.
    assert catalan_number(10)==16796'''
    
    # Check for non-positive integer input
    if num <= 0:
        return 1
    
    # Calculate catalan number using memoization
    catalan = [0] * (num+1)
    catalan[0] = 1
    
    for i in range(1, num+1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
    
    return catalan[num]
import unittest

class Test(unittest.TestCase):
    def test_catalan_number(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()