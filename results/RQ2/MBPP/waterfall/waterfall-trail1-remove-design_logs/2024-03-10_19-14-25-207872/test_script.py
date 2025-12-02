def rearrange_bigger(n):
    num_list = list(str(n))
    
    if sorted(num_list, reverse=True) == num_list:
        return n
    
    for i in range(len(num_list)-1, 0, -1):
        if num_list[i] > num_list[i-1]:
            num_list[i], num_list[i-1] = num_list[i-1], num_list[i]
            return int("".join(num_list))
    
    return n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()