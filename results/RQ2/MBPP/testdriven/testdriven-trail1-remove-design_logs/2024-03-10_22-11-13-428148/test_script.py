def union_elements(test_tup1, test_tup2):
    combined_tuple = test_tup1 + test_tup2
    unique_elements = set(combined_tuple)
    sorted_elements = tuple(sorted(unique_elements))
    return sorted_elements

# Test Cases:
def test_union_elements():
    assert union_elements((1, 2, 3),(2, 3, 4)) == (1, 2, 3, 4)
    assert union_elements(('a', 'b', 'c'),('b', 'c', 'd')) == ('a', 'b', 'c', 'd')
    assert union_elements((1, 'a', 2.5),('b', 3, 2.5)) == (1, 2.5, 3, 'a', 'b')
    assert union_elements((),()) == ()
    assert union_elements((None, None),(None, None)) == ()
    assert union_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10),(6, 7, 8, 9, 10, 11, 12, 13, 14, 15)) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(union_elements((3, 4, 5, 6), (5, 7, 4, 10)), (3, 4, 5, 6, 7, 10))

if __name__ == '__main__':
    unittest.main()