def find_tuples(test_list: list[tuple], K: int) -> list[tuple]:
    try:
        result = [tup for tup in test_list if all(ele % K == 0 for ele in tup)]
        return result
    except (TypeError, ZeroDivisionError):
        print("Invalid input type or value")
        return []
import unittest

class Test(unittest.TestCase):
    def test_find_tuples(self):
        self.assertEqual(find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6), [(6, 24, 12)])

if __name__ == '__main__':
    unittest.main()