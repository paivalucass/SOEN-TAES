def multiple_to_single(L):
    try:
         if not L:
             raise ValueError("Input list is empty")
         for item in L:
             if not isinstance(item, int):
                 raise ValueError("Input list contains non-numeric values")
         
         result = int(''.join(map(str, L)))
         return result
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()