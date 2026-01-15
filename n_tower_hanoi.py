import sys
import os

class IllegalMove(Exception):
    pass

class game:
    def __init__(self, rings, tower_amount):
        self.rings = rings
        self.tower_amount = tower_amount
        self.towers = [
            list(range(1, rings + 1)),
            *[[0]*rings for _ in range (tower_amount - 1)]
        ]
        #print(self.towers)
    
    def __str__(self):
        ascii_image = ""
        space_at_either_side_of_the_tower = " "*(self.rings)

        for i in range(self.tower_amount):
            ascii_image += space_at_either_side_of_the_tower
            ascii_image += "|"
            ascii_image += space_at_either_side_of_the_tower
            ascii_image += " "
        ascii_image += "\n"
        for ring in range(self.rings):
            for tower in range(self.tower_amount):
                ascii_image += " "* (self.rings - self.towers[tower][ring])
                ascii_image += "~"* (self.towers[tower][ring])
                ascii_image += "|"
                ascii_image += "~"* (self.towers[tower][ring])
                ascii_image += " "* (self.rings - self.towers[tower][ring])
                ascii_image += " "
            ascii_image += "\n"

        ascii_image += "="*(self.rings * 2 * self,tower_amount + (2 * self.tower_amount - 1))

        return ascii_image
    
    def move(self, origin, target):
        if origin not in list(range(self.tower_amount)) or target not in list(range(self.tower_amount)):
            raise IllegalMove
        if origin == target:
            raise IllegalMove
        
        origin_size = 0
        for i in range(self.rings):
            if self.towers[origin][i] != 0:
                origin_size = self.towers[origin][i]
                origin_position = i
                break
        if origin_size == 0:
            raise IllegalMove
        
        target_size = 0
        target_position = 0
        for i in range(self.rings):
            if self.towers[target][i] != 0:
                target_position = i
                target_size = self.towers[target][i]
                break
        
        if target_size != 0 and target_size < origin_size:
            raise IllegalMove
        
        self.towers[target][target_position -1] = origin_size
        self.towers[origin][origin_position] = 0
    
    
    def play_normal(self, target_tower, print_ui = True):
        if not print_ui:
            old_stdout = sys.stdout # backup current stdout
            sys.stdout = open(os.devnull, "w")
        
        print("Enter the number of the tower from wich you wanna move a ring and then the number of the tower where you want to move it to. Numbering starts at 0.")
        print()
        
        moves = 0
        while self.towers[target_tower] != list(range(1, self.rings + 1)):
            print("State:")
            print(self)
            
            user_input = input("Next Move: ")
            
            if user_input == "c":
                return "aborted by user"
            
            try:
                origin, target = map(int, user_input.split(" "))
            except:
                print("Move not recognized")
                print()
                continue
            
            try:
                self.move(origin, target)
                moves += 1
                print()
            except IllegalMove:
                print("Illegal move played.")
                print()
                continue
        
        print(f"Game finished in {moves} moves:")
        print("TODO: CALCULATE OPTIMAL MOVE COUNT N TOWERS")
        """
        if moves == 2**self.rings -1:
            print("Congratulation, you have found the optimal solution!")
        else:
            print(f"You're {self,moves - (2**self.rings - 1)} moves away from the optimal solution.")
        """
        print(self)
        print()

        if not print_ui:
            sys.stdout = old_stdout # reset old stdout

        return True





a = game(3)
a.play_normal()