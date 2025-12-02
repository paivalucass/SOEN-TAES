def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    try:
        start = planets.index(planet1)
        end = planets.index(planet2)
    except ValueError:
        return ()
    if start < end:
        return tuple(sorted(planets[start+1:end], key=lambda x: planets.index(x)))
    else:
        return tuple(sorted(planets[end+1:start], key=lambda x: planets.index(x)))

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(bf('Jupiter', 'Neptune'), ('Saturn', 'Uranus'))

    def test2(self):
        self.assertEqual(bf('Earth', 'Mercury'), ('Venus'))

    def test3(self):
        self.assertEqual(bf('Mercury', 'Uranus'), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn'))

    def test4(self):
        self.assertEqual(bf('Pluto', 'Mars'), ())

if __name__ == '__main__':
    unittest.main()