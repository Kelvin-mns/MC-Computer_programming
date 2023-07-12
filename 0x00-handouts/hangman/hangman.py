import random

def main():
    play_game()


class HangmanGame:
    def __init__(self):
        self .Word_list = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grapefruit"]
        self.Word = ""
        self.guessed_letters = []
        self.attempts = 6

    def start_game(self):
        self.word = random.choice(self.Word_list)
        self.guessed_letters = []
        self.attempts = 6

    def guess_letter(self, letter):
        if len(letter) != 1:
            return "please enter a single letter."

        if letter in self .guessed_letters:
            return "You have already guessed that letter. Try again."
        
        if letter not in self.word:
            self.attempts -= 1
            return "Incorrect guess. you have {} attempts left.".format(self.attempts)
        else:
            self.guessed_letters.append(letter)

        Word_progress = ""
        for char in self.Word:
            if char in self.guessed_letters:
                Word_progress += char + " "
            else:
                Word_progress  += "_"

        if "_" not in Word_progress:
            return "congratulation! you have guessed the word correcrtly."
        else:
            return Word_progress

def play_game():
    while True:
        game = HangmanGame()
        game.start_game()
        print("\nNew game! guess the word:")
        print(game.guess_letter(""))
        while game.attempts > 0:
            letter = input("Enter a letter: ")
            result = game.guess_letter(letter)
            print(result)
            if "congratulation" in result or "You ran out of attemps" in result:
                break

        play_gain = input("Do you want to play again? (yes/no): ")
        if play_gain.lower() != "yes":
            break

if __name__=="__main__":
    main()
