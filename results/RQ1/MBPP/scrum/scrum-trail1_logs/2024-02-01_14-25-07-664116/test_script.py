def freq_count(list1):
    if not isinstance(list1, list):
        raise TypeError("Input should be a list")

    if len(list1) == 0:
        return {}

    if len(list1) == 1:
        return {list1[0]: 1}

    if not all(isinstance(element, (int, str)) for element in list1):
        raise ValueError("List should contain only integers or strings")

    frequency_dict = {}
    for element in list1:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    return frequency_dict

# Test cases
assert freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]) == {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
assert freq_count([]) == {}
assert freq_count([10]) == {10: 1}
assert freq_count(['a','b','a','c','c']) == {'a': 2, 'b': 1, 'c': 2}
try:
    freq_count(123)
except TypeError as e:
    assert str(e) == "Input should be a list"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]), {10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

if __name__ == '__main__':
    unittest.main()