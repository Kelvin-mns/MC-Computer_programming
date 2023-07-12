import unittest
from hangman import HangmanGame
class HangmanGameTests(unittest.TestCase):
    def setUp(self):
        self.game.start_game()
        self.assertTrue(self.game.Word in self.game.Word_list)
        self.assertEqual(self.game.guessed_letter, [])
        self.assertEqual(self.game.attempts, 6)

    def test_guess_letter_correct(self):
        self.game.start_game()
        self.game.word = "apple"
        result = self.game.guess_letter("a")
        self.assertEqual(result, "a _ _ _ _")

    def test_guess_letter_incorrect(self):
        self.game.start_game()
        self.game.word = "apple"
        result = self.game.guess_letter("z")
        self.assertEqual(result, "Incorrect guess, You have 5 attempts left.")

    def test_guess_letter_already_guessed(self):
        self.game.start_game()
        self.game.word = "apple"
        self.game.guessed_letter = ["a" "p"]
        result = self.game.guess_letter("a")
        self.assertEqual(result, "You have already that letter. Try again.")
        
    def test_guess_letter_invalid_input(self):
        self.game.start_game()
        result = self.game.guess_letter("apple")
        self.assertEqual(result, "Please enter a single letter.")
        
    def test_game_win(self):
        self.game.start_game()
        self.game.word = ("apple")
        self.game.guessed_letter = ["a", "p", "l", "e"]
        result = self.game.guess_letter("a")
        self.assertEqual(result, "Congratulation! You guessed the word correctly.")

    def test_game_loss(self):
        self.game.start_game()
        self.game.word = "apple"
        self.game.guessed_letters = ["b", "c", "d", "f", "g"]
        result = self.game.guess_letter("a")
        self.assertEqual(result, "Incorrect guess. You have 1 attempt left.")

if __name__=="__main__":
    unittest.main()

