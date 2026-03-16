import random
from enum import Enum


class Move(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


class Player:
    def choose_move(self) -> Move:
        raise NotImplementedError


class HumanPlayer(Player):
    def choose_move(self) -> Move:
        choice = input("Enter rock, paper, scissors: ").strip().lower()
        if choice not in [m.value for m in Move]:
            raise ValueError("Invalid choice. Please try again!")

        return Move(choice)


class ComputerPlayer(Player):
    def choose_move(self) -> Move:
        return random.choice(list(Move))
