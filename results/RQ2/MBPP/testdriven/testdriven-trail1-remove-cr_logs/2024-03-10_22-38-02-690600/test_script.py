def start_with_p(words):
    '''Write a function to return two words from a list of words starting with letter 'p'.

    Input:
    - words: List of words

    Output:
    - Tuple of two words starting with letter 'p'
    '''

    p_words = [word for word in words.split() if word.lower().startswith('p')]
    if len(p_words) < 2:
        return ()
    else:
        return tuple(p_words[:2])
import unittest

class Test(unittest.TestCase):
    def test_start_withp(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()