def list_tuple(listx):
    if not isinstance(listx, list):
        raise ValueError("Input must be a list")
    
    if len(listx) == 0:
        raise ValueError("Input list cannot be empty")
    
    if any(type(x) != type(listx[0]) for x in listx):
        raise ValueError("Input list contains elements of different data types")
    
    return tuple(listx)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_tuple([5, 10, 7, 4, 15, 3]), (5, 10, 7, 4, 15, 3))

if __name__ == '__main__':
    unittest.main()