def list_split(input_list, step_size):
    if step_size <= 0 or step_size > len(input_list):
        return "Invalid step size"

    result = []
    for i in range(step_size):
        sublist = input_list[i::step_size]
        result.append(sublist)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3),
                         [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']])

if __name__ == '__main__':
    unittest.main()