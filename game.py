import random

class Game:
    def __init__(self, remaining_round=3):
        self.choices = ['rock', 'paper', 'scissors']
        self.computer_choice = None
        self.user_choice = None
        self.remaining_round = remaining_round

        self.user_score = 0
        self.computer_score = 0
        self.draw_count = 0

    def set_user_choice(self, choice):
        self.user_choice = choice

    def get_computer_choice(self):
        """Randomly selects the computer's choice."""
        self.computer_choice = random.choice(self.choices)

    def determine_winner(self):
        """Determines the winner based on the user's and computer's choices."""
        if self.user_choice == self.computer_choice:
            self.draw_count += 1
        elif (self.user_choice == 'rock' and self.computer_choice == 'scissors') or \
             (self.user_choice == 'paper' and self.computer_choice == 'rock') or \
             (self.user_choice == 'scissors' and self.computer_choice == 'paper'):
            self.user_score += 1
        else:
            self.computer_score += 1
        
    def playing(self):
        return self.remaining_round > 0

    def ready(self):
        self.get_computer_choice()

    def play(self):
        """Plays a round of Rock-Paper-Scissors."""
        result = self.determine_winner()
        self.remaining_round -= 1
        return result