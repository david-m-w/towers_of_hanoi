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
    
    def move(self):
        pass



a = game(3)
print(a)