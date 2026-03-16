from players import *


class Game:
    def __init__(self, rounds: int = 3):
        self.rounds = rounds
        self.human = HumanPlayer()
        self.computer = ComputerPlayer()
        self.scores = {"human": 0, "computer": 0}

    def decide_winner(self, human: Move, computer: Move):
        if human == computer:
            return "draw"
        wins = {
            Move.ROCK: Move.SCISSORS,
            Move.PAPER: Move.ROCK,
            Move.SCISSORS: Move.PAPER
        }

        return "human" if wins[human] == computer else "computer"
