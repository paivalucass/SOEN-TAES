def square_Sum(n):
    try:
        if n < 0 or not isinstance(n, int):
            raise ValueError("Input should be a non-negative integer")
        
        sum_of_squares = 0
        for i in range(1, 2*n, 2):
            sum_of_squares += i*i
        
        return sum_of_squares
    
    except ValueError as ve:
        return f"Invalid input: {ve}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 10)

if __name__ == '__main__':
    unittest.main()