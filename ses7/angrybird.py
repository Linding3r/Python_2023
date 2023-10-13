class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "S"
    
    def move_forward(self):
        if self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x -= 1
        elif self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1

        
    def turn(self):
        directions = ["N", "E", "S", "W"]
        index = directions.index(self.direction)
        self.direction = directions[(index - 1) % 4]

    def lose(self):
        print("Bird has lost!")

    def win(self):
        print("Bird has won!")


class Pig:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def lose(self):
        print("Pig has lost!")

    def win(self):
        print("Pig has won!")


class Board:

    def __init__(self):
        self.bird = Bird(2, 2)
        self.pig = Pig(7, 7)

    
    def display(self):
        for y in range(10):
            for x in range(10):
                if (x, y) == (self.bird.x, self.bird.y):
                    print("B", end="  ")
                elif (x, y) == (self.pig.x, self.pig.y):
                    print("P", end="  ")
                else:
                    print("*", end="  ")
            print()

class Workspace:
    def display(self):
        print("Instructions:\nM: Move Forward\nT: Turn\nB: Show Board\nQ: Quit")

    def get_commands(self):
        commands = input("Enter your commands: ")
        return list(commands)


class Game:
    def __init__(self):
        self.board = Board()
        self.workspace = Workspace()

    def display(self):
        self.board.display()
        self.workspace.display()

    def run(self):
        self.display()
        while True:
            commands = self.workspace.get_commands()
            for command in commands:
                if command == "m":
                    self.board.bird.move_forward()
                elif command == "t":
                    self.board.bird.turn()
                elif command == "b":
                    self.board.display()
                elif command == "q":
                    return
                if (self.board.bird.x, self.board.bird.y) == (self.board.pig.x, self.board.pig.y):
                    self.board.bird.win()
                    self.board.pig.lose()
                    return



game = Game()
game.run()


