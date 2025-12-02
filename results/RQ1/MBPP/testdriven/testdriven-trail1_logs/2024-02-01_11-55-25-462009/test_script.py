def is_samepatterns(colors, patterns):
    # Write a function to check whether it follows the sequence given in the patterns array.
    
    # Check if the length of colors and patterns are the same
    if len(colors) != len(patterns):
        return False
    
    # Create a dictionary to store the mapping of colors to patterns
    color_to_pattern = {}
    
    # Iterate through each color and pattern
    for color, pattern in zip(colors, patterns):
        # If the color is not in the dictionary, add it with the pattern as the value
        if color not in color_to_pattern:
            color_to_pattern[color] = pattern
        else:
            # If the color is in the dictionary but the pattern does not match, return False
            if color_to_pattern[color] != pattern:
                return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_samepatterns(["red","green","green"], ["a", "b", "b"]), True)

if __name__ == '__main__':
    unittest.main()