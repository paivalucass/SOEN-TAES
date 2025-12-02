import itertools

def combinations_colors(l, n):
    '''Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.'''
    return list(itertools.product(l, repeat=n))

# Test
assert combinations_colors(['Red', 'Green', 'Blue'], 1) == [('Red',), ('Green',), ('Blue',)]
import itertools

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(combinations_colors(["Red","Green","Blue"], 1), [('Red',), ('Green',), ('Blue',)])

if __name__ == '__main__':
    unittest.main()