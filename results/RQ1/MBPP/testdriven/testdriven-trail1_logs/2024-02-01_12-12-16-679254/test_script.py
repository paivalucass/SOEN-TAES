def find_even_pair(A):
    count = 0
    hashmap = {}
    for num in A:
        remainder = num % 2
        if remainder in hashmap:
            hashmap[remainder] += 1
        else:
            hashmap[remainder] = 1
    
    for num in A:
        complement = (num % 2) ^ 1
        if complement in hashmap:
            count += hashmap[complement]
    
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_even_pair([5, 4, 7, 2, 1]), 4)

if __name__ == '__main__':
    unittest.main()