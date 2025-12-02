def list_tuple(listx):
    try:
        if not isinstance(listx, list):
            raise TypeError("Input is not a valid list")
        return tuple(listx)
    except TypeError as e:
        return "Error: " + str(e)
    except Exception as e:
        return "An error occurred: " + str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_tuple([5, 10, 7, 4, 15, 3]), (5, 10, 7, 4, 15, 3))

if __name__ == '__main__':
    unittest.main()