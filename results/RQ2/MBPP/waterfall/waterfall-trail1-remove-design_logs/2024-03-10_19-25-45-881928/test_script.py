def pair_wise(l1):
    if len(l1) < 2:
        raise ValueError("Input list 'l1' must have at least two elements")
    
    if not all(isinstance(item, int) for item in l1):
        return "Error: Non-numeric items in input list"

    return [(l1[i], l1[i+1]) for i in range(len(l1)-1)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pair_wise([1,1,2,3,3,4,4,5]), [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)])

if __name__ == '__main__':
    unittest.main()