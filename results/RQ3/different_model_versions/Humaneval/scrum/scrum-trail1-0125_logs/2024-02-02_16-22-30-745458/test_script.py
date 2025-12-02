def make_a_pile(n):
    pile = []
    stones = n
    
    if not isinstance(n, int) or n < 0 or isinstance(n, float):
        return "Invalid Input"
    
    for i in range(n):
        pile.append(stones)
        if stones % 2 == 0:
            stones += 1
        else:
            stones += 2
    
    return pile

# Test cases
print(make_a_pile(0))  # Output: []
print(make_a_pile(1))  # Output: [1]
print(make_a_pile(3))  # Output: [3, 5, 7]
print(make_a_pile(1000))  # Output: [1000, 1002, 1004, ...]
print(make_a_pile(-5))  # Output: Invalid Input
print(make_a_pile(2.5))  # Output: Invalid Input
print(make_a_pile(1000000))  # Output: [1000000, 1000002, 1000004, ...]
import unittest

class Test(unittest.TestCase):
    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])
        self.assertEqual(make_a_pile(5), [5, 7, 9, 11, 13])

if __name__ == '__main__':
    unittest.main()