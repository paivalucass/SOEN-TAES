def list_tuple(listx):
    if isinstance(listx, list):
        return tuple(listx)
    else:
        raise ValueError("Input must be a list")

# Ensure input validation and add testing (not shown in the code snippet) to cover different scenarios as suggested.
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_tuple([5, 10, 7, 4, 15, 3]), (5, 10, 7, 4, 15, 3))

if __name__ == '__main__':
    unittest.main()