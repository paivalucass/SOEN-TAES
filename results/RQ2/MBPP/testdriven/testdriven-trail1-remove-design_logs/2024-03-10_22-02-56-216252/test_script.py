def newman_prime(n):
    '''
    Function to find the nth newman–shanks–williams prime number.
    '''
    if n <= 0:
        return "Invalid input"
    
    count = 0
    num = 2
    while True:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            count += 1
            if count == n:
                return num
        num += 1
import unittest

class Test(unittest.TestCase):
    def test_newman_prime(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()