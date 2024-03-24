import random

AMOUNT_OF_TRIES = int(input("Number of attempts: "))
changeDoors = bool(input("Change doors after first open? (True/False): "))
NUM_OF_DOORS = 3

class Door:
    def __init__(self) -> None:
        self.selected = False
        self.isWin = False

    def select(self):
        self.selected = True
    
    def winner(self):
        self.isWin = True

    def isSelected(self):
        return self.selected
    
    def isWinner(self):
        return self.isWin
    
    def swap(self):
        self.selected = not self.selected

class Game:
    def __init__(self, num_of_doors) -> None:
        self.doors = [Door() for _ in range(num_of_doors)]

        #choosing one door as the winner door
        random.choice(self.doors).winner()

        #choosing a door
        random.choice(self.doors).select()

        #removing a non-winner door
        for door in self.doors:
            if door.isSelected() is False and door.isWinner() is False:
                self.doors.remove(door)
                break

        # #swapping choice
        for door in self.doors:
            #door.swap() #comment this to prevent choice swapping
            pass

    def print(self):
        print(list(door.isSelected() for door in self.doors))

    def gameWon(self):
        won = False
        
        for door in self.doors:
            if door.isSelected() is True and door.isWinner() is True:
                won = True
                break

        return won

won_games = 0

for i in range(AMOUNT_OF_TRIES):
    game = Game(NUM_OF_DOORS)

    if game.gameWon() is True:
        won_games += 1

print("Chances: {:.2f}%".format((won_games/AMOUNT_OF_TRIES) * 100))
