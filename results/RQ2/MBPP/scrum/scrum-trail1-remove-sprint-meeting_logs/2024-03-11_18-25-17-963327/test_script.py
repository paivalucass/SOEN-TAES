import math
def find_solution(a, b, n):
    '''Write a function that returns integers x and y that satisfy ax + by = n as a tuple, or return None if no solution exists.
    assert find_solution(2, 3, 7) == (2, 1)'''
    if type(a) != int or type(b) != int or type(n) != int:
        return None
    
    if a < 0 or b < 0:
        return None
    
    if a == 0 and b == 0:
        return None
    
    if n % math.gcd(a, b) != 0:
        return None
    
    x, y = 0, 0
    while (n - b*y) % a != 0:
        y += 1
    
    x = (n - b*y) // a
    
    return (x, y)
import unittest

class Test(unittest.TestCase):
    def test_find_solution(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))

if __name__ == '__main__':
    unittest.main()