def even_Power_Sum(n): 
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    
    result = 0
    for i in range(1, n*2 + 1):
        if i % 2 == 0:
            result += i ** 5
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_Power_Sum(2), 1056)

if __name__ == '__main__':
    unittest.main()