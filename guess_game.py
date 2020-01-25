import random


class Guessing_Game:
    def __init__(self, guess, random_num, attempts, answer):
        self.guess = guess
        self.random_num = random_num
        self.attempts = attempts
        self.answer = answer

    def get_random_num(self):
        self.random_num = random.randint(1, 25)

    def guess_num(self):
        self.answer = False
        self.attempts = 0
        valid_attempt = False
        while not self.answer:
            try:
                guess = input("Guess an integer between 1 and 25: ")
                self.guess = int(guess)
                valid_attempt = True
            except ValueError:
                print("Invalid input. Guess an *integer* between 1 and 25. ")
            except type(self.guess) != int:
                print("Invalid input. Guess an *integer* between 1 and 25. ")
            if self.guess <= 0 or self.guess >= 26:
                print("Invalid input. Guess an integer between *1* and *25*. ")
            elif self.guess > self.random_num and valid_attempt:
                print("A little lower")
                self.attempts += 1
            elif self.guess < self.random_num and valid_attempt:
                print("A little higher")
                self.attempts += 1
            elif self.guess == self.random_num and valid_attempt:
                print("Correct!")
                self.attempts += 1
                print("It took you %d attempts to get it right." % self.attempts)
                self.answer = True


my_guessing_game = Guessing_Game(1, 3, 2, True)
my_guessing_game.get_random_num()
my_guessing_game.guess_num()
