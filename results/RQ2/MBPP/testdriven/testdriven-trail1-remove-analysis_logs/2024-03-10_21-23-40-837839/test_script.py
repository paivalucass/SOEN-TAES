def list_tuple(listx):
    if isinstance(listx, list) and listx:
        return tuple(listx)
    else:
        raise ValueError("Input is either not a list or an empty list")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_tuple([5, 10, 7, 4, 15, 3]), (5, 10, 7, 4, 15, 3))

if __name__ == '__main__':
    unittest.main()