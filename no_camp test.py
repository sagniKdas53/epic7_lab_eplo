import unittest
from no_camp import working


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input_c =
        result = 'Start,Normal tile,Normal tile,Normal tile,Camp tile with encounter,' \
                 'Normal tile,encounter,Normal tile,Normal tile,Normal tile,Normal tile,encounter,Normal tile,' \
                 'encounter,Normal tile,encounter,Normal tile,Normal tile,encounter,' \
                 'Normal tile,Camp tile with encounter,encounter,move to beginning,Normal tile,' \
                 'Normal tile,Normal tile,Normal tile,encounter,Normal tile,Normal tile,Normal tile,encounter,' \
                 'Normal tile,Normal tile,Normal tile,encounter,Normal tile,Normal tile,encounter,Normal tile,' \
                 'Normal tile,Camp tile with encounter,encounter,' \
                 '\nMoral Left:-24\nSteps taken:46\nEncounters:1\nCamp done:True'
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
