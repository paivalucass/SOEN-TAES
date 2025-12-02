def list_tuple(listx):
    try:
        if not isinstance(listx, list):
            raise TypeError("Input is not a list")
        for item in listx:
            if not isinstance(item, (int, float, str)):
                raise TypeError("List contains non-iterable elements")
    
        return tuple(listx)
    except Exception as e:
        print(f"Error: {e}")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_tuple([5, 10, 7, 4, 15, 3]), (5, 10, 7, 4, 15, 3))

if __name__ == '__main__':
    unittest.main()