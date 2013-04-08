try:
    from contextlib import contextmanager, GeneratorContextManager
except:
    # py 3
    from contextlib import contextmanager
    from contextlib import _GeneratorContextManager as GeneratorContextManager

import types
import unittest

X = 2
Y = 5

class TestContextManager(unittest.TestCase):
    def test_cm(self):
        # Context Managers
        #
        # Write a class style context manager ``plus_two`` that
        # adds 2 to a global ``X`` variable in the ``__enter__``
        # method, and subtracts 2 from X in the ``__exit__`` method
        # ================================

        self.assertTrue(isinstance(plus_two(), plus_two))
        with plus_two():
            self.assertEqual(X, 4)
        self.assertEqual(X, 2)


        # Context Managers
        #
        # Write a generator style context manager ``plus_five`` that
        # adds 5 to a global ``Y`` before execution of the body
        # and subtracts 5 from Y after the body
        # ================================

        print(type(plus_five()))
        self.assertTrue(isinstance(plus_five(), GeneratorContextManager))
        with plus_five():
            self.assertEqual(Y, 10)
        self.assertEqual(Y, 5)


if __name__ == '__main__':
    unittest.main()
