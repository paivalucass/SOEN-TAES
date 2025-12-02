def square_Sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"
    
    result = sum(i*i for i in range(2, (n*2)+1, 2))
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(2), 20)

if __name__ == '__main__':
    unittest.main()