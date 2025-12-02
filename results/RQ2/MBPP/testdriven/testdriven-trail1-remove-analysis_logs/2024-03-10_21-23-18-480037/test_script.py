def surface_Area(base_edge, height):
    ''' 
    This function calculates the surface area of a square pyramid using the provided base edge and height.
    Parameters:
    base_edge (int): The length of the base edge of the square pyramid.
    height (int): The height of the square pyramid.
    Returns:
    int: The surface area of the square pyramid.
    Raises:
    ValueError: If non-numeric inputs are provided.
    '''
    if isinstance(base_edge, (int, float)) and isinstance(height, (int, float)):
        if base_edge <= 0 or height <= 0:
            return "Invalid Input"
        else:
            return base_edge**2 + 2*base_edge*height
    else:
        raise ValueError("Non-numeric inputs are not allowed")

# Test cases
assert surface_Area(3, 4) == 33
# Add more test cases as per the suggestions from the tester role.
import unittest

class Test(unittest.TestCase):
    def test_surface_area(self):
        self.assertEqual(surface_Area(3, 4), 33)

if __name__ == '__main__':
    unittest.main()