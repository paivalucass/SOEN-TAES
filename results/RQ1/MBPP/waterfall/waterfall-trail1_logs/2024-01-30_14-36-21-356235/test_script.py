def sort_counter(dict1):
    if not isinstance(dict1, dict):
        raise TypeError("Input is not a dictionary")
    
    if len(dict1) == 0:
        return []

    sorted_items = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    return sorted_items
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}), [('Chemistry', 87), ('Physics', 83), ('Math', 81)])

if __name__ == '__main__':
    unittest.main()