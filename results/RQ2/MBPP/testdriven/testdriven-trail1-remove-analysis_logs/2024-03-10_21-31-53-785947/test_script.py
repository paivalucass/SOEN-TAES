def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_ludic(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"
    
    ludic_numbers = []
    for i in range(1, n+1):
        if is_prime(i):
            ludic_numbers.append(i)
    
    return ludic_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()