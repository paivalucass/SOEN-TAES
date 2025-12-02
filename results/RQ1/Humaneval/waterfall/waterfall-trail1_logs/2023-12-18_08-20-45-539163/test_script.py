def add(lst):
    if not lst:
        return 0
    
    even_sum = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
    
    return even_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

if __name__ == '__main__':
    unittest.main()