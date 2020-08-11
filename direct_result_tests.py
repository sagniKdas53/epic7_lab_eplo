import unittest
from the_real_main_function import working


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = '\nMoral Left:-24\nSteps taken:46\nEncounters:11\nCamp done:True'
        self.assertEqual(working('s   c n x   n n n  n cnb   x n   n x  n  n  cn', 40, False),result)

if __name__ == '__main__':
    unittest.main()
