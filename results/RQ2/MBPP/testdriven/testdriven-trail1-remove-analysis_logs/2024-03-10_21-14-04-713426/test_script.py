def combinations_colors(colors, length):
    '''Generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.'''
    if not isinstance(colors, list) or not colors:
        return "Invalid input"
    if not isinstance(length, int) or length <= 0:
        return "Invalid input"
    
    result = []
    
    def generate_combinations(current, index):
        if len(current) == length:
            result.append(tuple(current))
            return
        for i in range(len(colors)):
            generate_combinations(current + [colors[i]], i)
    
    generate_combinations([], 0)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_combinations_colors(self):
        self.assertEqual(combinations_colors(["Red","Green","Blue"], 1), [('Red',), ('Green',), ('Blue',)])

if __name__ == '__main__':
    unittest.main()