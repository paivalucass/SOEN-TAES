def list_tuple(listx):
    if not isinstance(listx, list):
        raise ValueError("Input is not a list")

    result_tuple = tuple(listx)
    
    return result_tuple
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_tuple([5, 10, 7, 4, 15, 3]), (5, 10, 7, 4, 15, 3))

if __name__ == '__main__':
    unittest.main()