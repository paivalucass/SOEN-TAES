from typing import Union

def volume_cube(l: Union[int, float]) -> Union[int, float]:
    '''This function calculates the volume of a cube based on the length of its side'''
    if not isinstance(l, (int, float)) or l < 0:
        return "Error: Invalid input. Please provide a valid positive number for side length."

    volume = l ** 3
    return volume
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()