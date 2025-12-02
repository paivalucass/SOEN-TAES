def list_tuple(listx):
    try:
        if type(listx) != list or len(listx) == 0:
            raise ValueError("Input is not a non-empty list")

        return tuple(listx)
    except ValueError as ve:
        return ve.args[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_tuple([5, 10, 7, 4, 15, 3]), (5, 10, 7, 4, 15, 3))

if __name__ == '__main__':
    unittest.main()