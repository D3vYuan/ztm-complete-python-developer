import unittest
import random_game

class TestGame(unittest.TestCase):
    def test_input_true(self):
        '''
        INFO: Test input is true
        '''
        answer = 5
        guess = 5
        result = random_game.run_guess(answer=answer, guess=guess)
        self.assertTrue(result)

    def test_input_false_smaller(self):
        '''
        INFO: Test input is false
        '''
        answer = 5
        guess = 0
        result = random_game.run_guess(answer=answer, guess=guess)
        self.assertFalse(result)

    def test_input_oob(self):
        '''
        INFO: Test input Out of Bound
        '''
        answer = 5
        guess = 11
        result = random_game.run_guess(answer=answer, guess=guess)
        self.assertFalse(result)

    def test_input_string(self):
        '''
        INFO: Test input is String
        '''
        answer = 5
        guess = '11'
        result = random_game.run_guess(answer=answer, guess=guess)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()