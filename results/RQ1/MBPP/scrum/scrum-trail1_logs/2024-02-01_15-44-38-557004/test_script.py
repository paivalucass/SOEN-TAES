def multiple_to_single(L):
    if not isinstance(L, list):
        return "Error: Input is not a list"
    if len(L) == 0:
        return "Error: Input list is empty"
    for num in L:
        if not isinstance(num, int):
            return "Error: Non-integer values are not allowed"
    
    combined_value = int(''.join(map(str, L)))
    return combined_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()