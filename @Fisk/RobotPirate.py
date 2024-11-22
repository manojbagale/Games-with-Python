class RobotPirate:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.num_treasures = 5
        self.row = 0
        self.col = 0
        self.direction = "S"
        self.treasure_locations = set()

    def __str__(self):
        room = [['-' for x in range(self.width)] for x in range(self.height)]
        for r, c in self.treasure_locations:
            room[r][c] = "x"
        room[self.row][self.col] = self.name[0].upper()
        return '\n'.join("".join(row) for row in room)
        
    def __eq__(self, other):
        return (self.row == other.row and self.col == other.col) and (self.direction == other.direction)
    
    def drop_treasure(self):
        if self.num_treasures > 0 and (self.row, self.col) not in self.treasure_locations:
            self.treasure_locations.add((self.row, self.col))
            self.num_treasures -= 1
            return True
        return False
    
    def move(self, places):

        if self.direction == "S":
            self.row = min(self.row + places, self.height-1) 
        elif self.direction == "E":
            self.col = min(self.col + places, self.width-1)
        elif self.direction == "W":
            self.col = max(0, self.col - places)
        elif self.direction == "N":
            self.row = max(0, self.row - places)

        current_location = (self.row, self.col)
        if current_location in self.treasure_locations:
            self.treasure_locations.remove(current_location)
            self.num_treasures += 1
            
    def turn_left(self):
        if self.direction == "S":
            self.direction = "E"
        elif self.direction == "N":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "W":
            self.direction = "S"
    
    def turn_right(self):
        if self.direction == "S":
            self.direction = "W"
        elif self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "W":
            self.direction = "N"

def run_program():
    robot = RobotPirate("Pirate Jake", 5, 3)
    keep_playing = 'y'
    while keep_playing == 'y':
        question = "What would you like to do: "
        m = "Options:\n  m: move forward"
        d = "  d: drop treasure"
        l = "  l: turn left"
        r = "  r: turn right"
        q = "  q: quit"
        prompt = "{}\n{}\n{}\n{}\n{}\n{}".format(m, d, l, r, q, question)
        action = input(prompt)
        if action == 'm':
            how_many = int(input('How many spots? '))
            robot.move(how_many)
        elif action == 'd':
            robot.drop_treasure()
        elif action == 'l':
            robot.turn_left()
        elif action == 'r':
            robot.turn_right()
        elif action == 'q':
            keep_playing = 'n'
        print(robot)
    print('All done!')

if __name__ == "__main__":
    run_program()
