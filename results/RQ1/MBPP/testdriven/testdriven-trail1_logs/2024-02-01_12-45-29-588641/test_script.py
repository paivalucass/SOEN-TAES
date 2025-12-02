def multiple_to_single(L):
    for i in L:
        if not isinstance(i, int):
            return "Error: Invalid Input"
    
    joined_string = ''.join(str(i) for i in L)
    try:
        result = int(joined_string)
        return result
    except ValueError:
        return "Error: Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()