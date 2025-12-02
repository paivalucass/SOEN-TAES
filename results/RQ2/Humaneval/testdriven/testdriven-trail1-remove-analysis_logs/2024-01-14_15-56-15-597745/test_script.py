def exchange(lst1, lst2):
    odd_lst1 = [num for num in lst1 if num % 2 != 0]
    odd_lst2 = [num for num in lst2 if num % 2 != 0]
    if len(odd_lst1) > len(odd_lst2):
        return 'NO'
    return 'YES'
import unittest

class Test(unittest.TestCase):
    def test_exchange(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

if __name__ == '__main__':
    unittest.main()