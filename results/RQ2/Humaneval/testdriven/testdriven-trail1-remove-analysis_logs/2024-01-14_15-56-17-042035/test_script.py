def histogram(test):
    """
    Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """

    def clean_input(input_str):
        return input_str.replace(" ", "")

    def is_lowercase(input_str):
        return input_str.islower()

    def count_letters(input_str):
        result = {}
        for letter in input_str:
            if letter in result:
                result[letter] += 1
            else:
                result[letter] = 1
        return result

    def get_max_letters(input_dict):
        max_count = max(input_dict.values())
        return {key: value for key, value in input_dict.items() if value == max_count}

    if not isinstance(test, str):
        return {}

    test = clean_input(test)

    if not is_lowercase(test):
        return {}

    result = count_letters(test)
    
    return get_max_letters(result)
import unittest

class Test(unittest.TestCase):
    def test_histogram(self):
        self.assertEqual(histogram('a b c'), {'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(histogram('a b b a'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('a b c a b'), {'a': 2, 'b': 2})
        self.assertEqual(histogram('b b b b a'), {'b': 4})
        self.assertEqual(histogram(''), {})

if __name__ == '__main__':
    unittest.main()