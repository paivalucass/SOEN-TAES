def split(word):
    '''
    Write a python function to split a string into characters.
    assert split('python') == ['p','y','t','h','o','n']
    '''
    import unittest
    if word is None or not isinstance(word, str):
        raise ValueError("Invalid input data: Input should be a non-empty string")
    return list(word)
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split('python'), ['p','y','t','h','o','n'])

if __name__ == '__main__':
    unittest.main()