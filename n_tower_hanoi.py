import sys
import os
import random as r

class IllegalMove(Exception):
    pass
class TargetOutOfBounds(Exception):
    pass
class TargetNotSet(Exception):
    pass


class game:
    def __init__(self, rings, tower_amount, target = None, state = "default"):
        self.rings = rings
        self.tower_amount = tower_amount
        self.set_target(target)
        self.set_gamestate(state)
    
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

        if self.target == None:
            ascii_image += "="*(self.rings * 2 * self.tower_amount + (2 * self.tower_amount - 1))
        else:
            ascii_image += "="*(self.rings * 2 * self.target + (2 * self.target))
            ascii_image += "#"*(self.rings * 2 + 1)
            ascii_image += "="*(self.rings * 2 * (self.tower_amount - self.target - 1) + (2 * (self.tower_amount - self.target - 1)))

        return ascii_image
    
    def set_target(self, target):
        if target < 0 or target >= self.tower_amount:
            raise TargetOutOfBounds
        self.target = target
    
    def set_gamestate(self, state):
        match state:
            case "default":
                self.towers = [
                    list(range(1, self.rings + 1)),
                    *[[0]*self.rings for _ in range (self.tower_amount - 1)]
                ]
            
            case "default_illegal":
                self.towers = [
                    list(range(self.rings, 0, -1)),
                    *[[0]*self.rings for _ in range (self.tower_amount - 1)]
                ]
            
            case "random_legal":
                self.towers = [[] for _ in range(self.tower_amount)]
                for ring in range(1, self.rings + 1):
                    self.towers[r.randint(0, self.tower_amount-1)].append(ring)
                for i in range(self.tower_amount):
                    self.towers[i] = [0]*(self.rings - len(self.towers[i])) + self.towers[i]
            
            case "random_illegal_on_purpose":
                self.towers = [[] for _ in range(self.tower_amount)]
                for ring in range(1, self.rings + 1):
                    self.towers[r.randint(0, self.tower_amount-1)].append(ring)
                for i in range(self.tower_amount):
                    self.towers[i].reverse()
                for i in range(self.tower_amount):
                    self.towers[i] = [0]*(self.rings - len(self.towers[i])) + self.towers[i]
            
            case "total_random":
                self.towers = [[] for _ in range(self.tower_amount)]
                rings_shuffeld = list(range(1, self.rings + 1))
                r.shuffle(rings_shuffeld)
                for ring in rings_shuffeld:
                    self.towers[r.randint(0, self.tower_amount-1)].append(ring)
                for i in range(self.tower_amount):
                    self.towers[i] = [0]*(self.rings - len(self.towers[i])) + self.towers[i]
            
            case _:
                raise SyntaxError
    
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
    
    def play_normal(self, print_ui = True):
        if self.target == None:
            raise TargetNotSet
        
        if not print_ui:
            old_stdout = sys.stdout # backup current stdout
            sys.stdout = open(os.devnull, "w")
        
        print("Enter the number of the tower from wich you wanna move a ring and then the number of the tower where you want to move it to. Numbering starts at 0.")
        print()
        
        moves = 0
        while self.towers[self.target] != list(range(1, self.rings + 1)):
            print("State:")
            print(self)
            print(f"Moves used: {moves}")
            
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





a = game(12, 6, 3, state="total_random")
print(a)

"""

1, 4, 3
0, 3

2, 4, 3
0, 1
0, 3
1, 3

3, 4, 3
0, 1
0, 2
0, 3
2, 3
1, 3

4, 4, 3
0, 1
0, 2
1, 2
0, 1
0, 3
1, 3
2, 1
2, 3
1, 3


"""