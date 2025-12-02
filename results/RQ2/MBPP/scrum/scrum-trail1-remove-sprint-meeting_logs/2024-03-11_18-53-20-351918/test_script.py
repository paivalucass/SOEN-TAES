def empty_list(length):
    try:
        n = int(length)
    except ValueError:
        raise ValueError("Input length must be a valid integer")
   
    if n < 0:
        raise ValueError("Input length must be a non-negative integer")
       
    result = [{} for _ in range(n)]
   
    return result
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(empty_list(5), [{},{},{},{},{}])

if __name__ == '__main__':
    unittest.main()