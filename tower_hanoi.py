class IllegalMove(Exception):
    pass

class game:
    def __init__(self, rings):
        self.rings = rings
        self.towers = [
            list(range(1, rings + 1)),
            [0]*rings,
            [0]*rings
        ]
        #print(self.towers)
    
    def __str__(self):
        ascii_image = ""
        space_at_either_side_of_the_tower = " "*(self.rings)

        for i in range(3):
            ascii_image += space_at_either_side_of_the_tower
            ascii_image += "|"
            ascii_image += space_at_either_side_of_the_tower
            ascii_image += " "
        ascii_image += "\n"
        for ring in range(self.rings):
            for tower in range(len(self.towers)):
                ascii_image += " "* (self.rings - self.towers[tower][ring])
                ascii_image += "~"* (self.towers[tower][ring])
                ascii_image += "|"
                ascii_image += "~"* (self.towers[tower][ring])
                ascii_image += " "* (self.rings - self.towers[tower][ring])
                ascii_image += " "
            ascii_image += "\n"

        ascii_image += "="*(self.rings * 6 + 5)
        ascii_image += "\n"

        return ascii_image
    
    def move(self, origin, target):
        if origin not in [0,1,2] or target not in [0,1,2]:
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
    
    def play_normal(self, target_tower = 2, print_state = True):
        move count = 0
        while self.towers[target_tower] != list(range(self.rings)):
            print("State:")
            print(self)
            try:
                origin, target = map(int, input("Next Move: ").split(" "))
            except:
                print("Move not recognized")
                print()
                continue
            
            try:
                self.move(origin, target)
                moves += 1
            except IllegalMove:
                print("Illegal move played.")
                print()
                continue
        
        print(f"Game finished in {moves} moves:")
        if moves == 2**self.rings -1:
            print("Congratulation, you have found the optimal solution!")
        else:
            print(f"You're {self,moves - (2**n - 1)} moves away from the optimal solution.")
        print(self)
        print()





a = game(3)
print(a)
a.move(0, 2)
print(a)
a.move(0, 1)
print(a)
a.move(2, 1)
print(a)
a.move(0, 2)
print(a)
a.move(1, 0)
print(a)
a.move(1, 2)
print(a)
a.move(0, 2)
print(a)
