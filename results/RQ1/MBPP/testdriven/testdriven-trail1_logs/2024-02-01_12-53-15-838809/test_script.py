import logging

def sort_counter(dict1):
    try:
        if not isinstance(dict1, dict) or not all(isinstance(val, int) for val in dict1.values()):
            raise ValueError("Input dictionary is either empty or contains non-integer values")
        
        sorted_tuples = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        logging.info(f"Input dictionary: {dict1}, Sorted output: {sorted_tuples}")
        return sorted_tuples
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}), [('Chemistry', 87), ('Physics', 83), ('Math', 81)])

if __name__ == '__main__':
    unittest.main()