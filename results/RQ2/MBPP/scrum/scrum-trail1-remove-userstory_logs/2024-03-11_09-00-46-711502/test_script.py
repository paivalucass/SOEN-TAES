def count_X(tup, x):
    try:
        if not isinstance(tup, tuple):
            raise ValueError("Input must be a tuple")
        if len(tup) == 0:
            return 0
        
        count_dict = {}
        for element in tup:
            if element in count_dict:
                count_dict[element] += 1
            else:
                count_dict[element] = 1
        
        return count_dict.get(x, 0)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4), 0)

if __name__ == '__main__':
    unittest.main()