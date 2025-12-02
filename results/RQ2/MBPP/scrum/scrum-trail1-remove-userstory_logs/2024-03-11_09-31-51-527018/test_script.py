def get_ludic(n):
    def is_lucid(num):
        if num < 1:
            return False
        if num == 1:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    if n < 1:
        return "Error: Invalid input"
    
    lucid_numbers = [i for i in range(1, n+1) if is_lucid(i)]
    
    return lucid_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()