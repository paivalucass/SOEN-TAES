def add_pairwise(test_tup):
    result = []
    for i in range(len(test_tup)-1):
        try:
            pair_sum = test_tup[i] + test_tup[i+1]
            result.append(pair_sum)
        except IndexError:
            print("Error: Tuple index out of range")
        except TypeError:
            print("Error: Invalid input type")
    
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_pairwise((1, 5, 7, 8, 10)), (6, 12, 15, 18))

if __name__ == '__main__':
    unittest.main()