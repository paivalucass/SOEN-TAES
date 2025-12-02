def perfect_squares(a, b):
    '''
    Write a function to find perfect squares between two given numbers.
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
    '''
    
    if a > b:
        raise ValueError("'a' cannot be greater than 'b'")
    if a < 0 or b < 0:
        raise ValueError("Both 'a' and 'b' must be positive numbers")
    
    result = []
    for num in range(a, b+1):
        if num >= 0 and int(num**0.5)**2 == num:
            result.append(num)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perfect_squares(1,30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()