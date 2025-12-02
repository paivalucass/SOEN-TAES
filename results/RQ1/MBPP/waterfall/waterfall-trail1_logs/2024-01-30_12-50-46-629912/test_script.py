def newman_prime(n): 
    '''Write a function to find the nth newman–shanks–williams prime number.'''
    if n <= 0:
        raise ValueError("Input n must be a positive integer")

    count = 0
    num = 1

    while count < n:
        num += 1
        if is_newman_shanks_williams_prime(num):
            count += 1

    return num

def is_newman_shanks_williams_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

assert newman_prime(3) == 7
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(newman_prime(3), 7)

if __name__ == '__main__':
    unittest.main()