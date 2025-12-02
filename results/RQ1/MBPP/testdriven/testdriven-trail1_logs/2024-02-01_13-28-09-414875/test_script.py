def unique_sublists(input_list):
    # Convert every list to a tuple
    tuple_list = [tuple(sublist) for sublist in input_list if isinstance(sublist, list)]
    
    # Count the occurrences of each tuple
    tuple_counts = {t: tuple_list.count(t) for t in set(tuple_list)}
    
    return tuple_counts
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()