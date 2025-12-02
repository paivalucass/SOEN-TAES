def square_Sum(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid Input"
    
    if n == 0:
        return 0
    
    sum_of_squares = 0
    for i in range(1, (n*2)+1):
        if i % 2 == 0:
            sum_of_squares += i**2
    
    return sum_of_squares
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 20)

if __name__ == '__main__':
    unittest.main()