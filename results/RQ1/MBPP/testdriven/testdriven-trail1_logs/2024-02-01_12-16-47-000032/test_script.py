def volume_cube(side_length):
    '''Write a function to find the volume of a cube given its side length.
    assert volume_cube(3)==27'''
    
    if not isinstance(side_length, (int, float)):
        return "Error: Input is not a number"
    elif side_length <= 0:
        return "Error: Side length should be a positive number"
    else:
        return side_length * side_length * side_length
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()