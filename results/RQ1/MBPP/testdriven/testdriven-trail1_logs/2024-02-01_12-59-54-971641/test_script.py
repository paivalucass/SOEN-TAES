def catalan_number(num):
    '''
    Write a function which returns nth catalan number.
    assert catalan_number(10)==16796
    '''
    if type(num) != int or num < 0:
        return "Invalid input"
    
    if num == 0:
        return 1
    
    catalan_numbers = [0]*(num+1)
    catalan_numbers[0] = 1
    
    for i in range(1, num+1):
        catalan_numbers[i] = 0
        for j in range(i):
            catalan_numbers[i] += catalan_numbers[j] * catalan_numbers[i-j-1]
    
    return catalan_numbers[num]
import unittest

class Test(unittest.TestCase):
    def test_catalan_number(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()