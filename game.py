import random

class Game:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.computer_choice = None
        self.user_choice = None

    def set_user_choice(self, choice):
        self.user_choice = choice

    def get_computer_choice(self):
        """Randomly selects the computer's choice."""
        self.computer_choice = random.choice(self.choices)

    def determine_winner(self):
        """Determines the winner based on the user's and computer's choices."""
        if self.user_choice == self.computer_choice:
            return "It's a tie!"
        elif (self.user_choice == 'rock' and self.computer_choice == 'scissors') or \
             (self.user_choice == 'paper' and self.computer_choice == 'rock') or \
             (self.user_choice == 'scissors' and self.computer_choice == 'paper'):
            return "You win!"
        else:
            return "Computer wins!"

    def ready(self):
        self.get_computer_choice()

    def play(self):
        """Plays a round of Rock-Paper-Scissors."""
        print(f"User chose: {self.user_choice}")
        print(f"Computer chose: {self.computer_choice}")
        print(f"------------------------------------------")
        result = self.determine_winner()
        return result