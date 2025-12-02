def cal_sum(n):
    '''
    Write a function to calculate the sum of Perrin numbers.
    assert cal_sum(9) == 49
    '''
    perrin = [3, 0, 2]
    
    if not isinstance(n, int) or n < 0:
        return "Invalid Input"
    
    for i in range(3, n+1):
        p_sum = perrin[i-2] + perrin[i-3]
        perrin.append(p_sum)
    
    return perrin[n-1]
import unittest

class Test(unittest.TestCase):
    def test_cal_sum(self):
        self.assertEqual(cal_sum(9), 49)

if __name__ == '__main__':
    unittest.main()