def surfacearea_cube(l):
    """
    Function to calculate the surface area of a cube of a given size.
    :param l: size of the cube
    :return: surface area of the cube
    """
    if not isinstance(l, (int, float)):
        return "Invalid Input"
    
    if l in memoized_surface_area:
        return memoized_surface_area[l]
    
    surface_area = 6 * (l * l)
    
    memoized_surface_area[l] = surface_area
    
    return surface_area

memoized_surface_area = {}

# Test cases
assert surfacearea_cube(5) == 150
assert surfacearea_cube(3) == 54
assert surfacearea_cube(10) == 600
assert surfacearea_cube(0) == 0
assert surfacearea_cube(1) == 6
assert surfacearea_cube('abc') == "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test_surfacearea_cube(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()