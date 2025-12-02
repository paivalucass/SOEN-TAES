def bf(planet1, planet2):
    planets = {
        "Mercury": 1,
        "Venus": 2,
        "Earth": 3,
        "Mars": 4,
        "Jupiter": 5,
        "Saturn": 6,
        "Uranus": 7,
        "Neptune": 8
    }

    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        start_index = planets[planet1]
        end_index = planets[planet2]
        result = []
        if start_index < end_index:
            for i in range(start_index+1, end_index):
                result.append(list(planets.keys())[i-1])
        else:
            for i in range(end_index+1, start_index):
                result.append(list(planets.keys())[i-1])
        return tuple(result)

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))

    def test2(self):
        self.assertEqual(bf("Earth", "Mercury"), ("Venus"))

    def test3(self):
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))

    def test4(self):
        self.assertEqual(bf("Mercury", "Pluto"), ())

if __name__ == '__main__':
    unittest.main()