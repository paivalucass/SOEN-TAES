def multiple_to_single(L):
    if not all(isinstance(x, int) for x in L):
        raise ValueError("Input list should only contain integers")
    
    if len(L) == 0:
        return 0
    
    result = "".join(str(num) for num in L)
    
    return int(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()