def exchange(lst1, lst2):
    even_numbers_lst1 = [x for x in lst1 if x % 2 == 0]
    odd_numbers_lst2 = [x for x in lst2 if x % 2 != 0]
    
    return "YES" if len(even_numbers_lst1) >= len(odd_numbers_lst2) else "NO"
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test2(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

if __name__ == '__main__':
    unittest.main()