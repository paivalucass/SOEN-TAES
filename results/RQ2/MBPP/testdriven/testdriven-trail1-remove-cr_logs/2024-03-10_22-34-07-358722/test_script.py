def volume_cube(l):
    '''
    Function to find the volume of a cube given its side length.
    assert volume_cube(3) == 27
    '''
    if type(l) != int:
        return "Error: Invalid input for side length"
    if l < 0:
        return "Error: Invalid input for side length"
    return l ** 3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()