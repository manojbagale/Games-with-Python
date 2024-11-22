import random

class Wordle:

    count = 0
    word_bank = ["banjo"]
    num_wins = 0
    num_losses = 0

    def __init__(self, num_guesses):
        self.num_guesses = num_guesses
        self.word = random.choice(self.word_bank) 
        self.guesses = []
    
    def __str__(self):
        status = ""
        n = 0
        while n < len(self.guesses):
            guessed_word = [x.upper() for x in self.guesses[n]]
            actual_word = [x.upper() for x in self.word]
            for g_ltr in guessed_word: 
                if g_ltr in actual_word:
                    if guessed_word.index(g_ltr) == actual_word.index(g_ltr):
                        status += g_ltr.upper() + "(g)" + " "
                    elif g_ltr in actual_word:
                        status += g_ltr.upper() + "(y)" + " "
                else:
                        status += g_ltr.upper() + "(r)" + " "
            status += "\n"
            n += 1
        return status + f"{self.num_guesses} guesses remaining"
            
    def make_guess(self, guess):
        self.num_guesses -= 1
        if len(guess) != 5:
            print("Guess must be exactly 5 letters. Try again")
            return False
        if len(set(guess)) != len(list(guess)):
            print("Guess must contain unique letters only. Try again")
            return False
        self.guesses.append(guess)
        if guess.lower() == self.word.lower():
            print("You win")
            Wordle.num_wins += 1
            return True
        if self.num_guesses == 0 and guess != self.word:
            print("You lose")
            Wordle.num_losses += 1
            return True
        return False

def run_program():
    play_again = 'y'
    while play_again == 'y':
        wordle_game = Wordle(6)
        print(wordle_game)
        game_over = False
        while not game_over:
            guess = input('What is your guess? ')
            game_over = wordle_game.make_guess(guess)
            print(wordle_game)
        print("Wins: {}, Losses: {}".format(Wordle.num_wins, Wordle.num_losses))
        print()
        play_again = input("Play again(y/n)? ")
        print()
    print("All done!")

if __name__ == "__main__":
    run_program()
