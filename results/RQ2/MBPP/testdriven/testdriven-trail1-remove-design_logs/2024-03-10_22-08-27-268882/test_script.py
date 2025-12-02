def surfacearea_cube(l):
    '''
    Write a function to find the surface area of a cube of a given size.
    assert surfacearea_cube(5)==150
    '''
    try:
        if isinstance(l, int) and l > 0:
            return 6 * (l ** 2)
        else:
            return "Error: Invalid input"
    except Exception as e:
        return "Error: Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()