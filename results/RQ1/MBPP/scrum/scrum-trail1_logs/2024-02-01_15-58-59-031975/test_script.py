def sort_counter(dict1):
    return sorted(dict1.items(), key=lambda x: x[1], reverse=True)
import unittest

class Test(unittest.TestCase):
    def test_sort_counter(self):
        self.assertEqual(sort_counter({'Math':81, 'Physics':83, 'Chemistry':87}), [('Chemistry', 87), ('Physics', 83), ('Math', 81)])

if __name__ == '__main__':
    unittest.main()