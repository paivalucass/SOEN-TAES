def square_Sum(n):
    try:
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        
        if n <= 0:
            raise ValueError("Input must be a positive integer")
        
        sum = 0
        for i in range(1, n+1):
            sum += (2*i)**2
        
        return sum
    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 20)

if __name__ == '__main__':
    unittest.main()