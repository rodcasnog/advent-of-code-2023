with open('./advent-of-code/advent-of-code_16.txt') as f:
    data = f.read()

data = data.strip().split("\n")

# Part 1

class beam():
    
    def __init__(self, x, y, direction, number=0):
        self.x = x
        self.y = y
        self.direction = direction
        self.number = number
        # print('Created ', self)

    def __repr__(self):
        return f'Beam {self.number}: (x={self.x}, y={self.y}, direction={self.direction})'

    def run(self, data, sol, visited):

        while self.x < 110 and self.y < 110 and self.x > -1 and self.y > -1:
            
            if self.direction in visited[self.y][self.x]:
                # print(self, 'has visited again', visited[self.y][self.x])
                return
            else:
                visited[self.y][self.x].append(self.direction)
                # print(self, 'visits', visited[self.y][self.x])

            
            # print(self.x, self.y, self.direction, data[self.y][self.x], sol[self.y][self.x])
            sol[self.y][self.x] = 1
        
            if data[self.y][self.x] == '.':
                if self.direction == 'up':
                    self.y-=1
                elif self.direction == 'down':
                    self.y+=1
                elif self.direction == 'left':
                    self.x-=1
                elif self.direction == 'right':
                    self.x+=1
            elif data[self.y][self.x] == '\\':
                # print(self, 'hit \\')
                if self.direction == 'up':
                    self.x-=1
                    self.direction = 'left'
                elif self.direction == 'down':
                    self.x+=1
                    self.direction = 'right'
                elif self.direction == 'left':
                    self.y-=1
                    self.direction = 'up'
                elif self.direction == 'right':
                    self.y+=1
                    self.direction = 'down'
                # print(self, 'after \\')
            elif data[self.y][self.x] == '/':
                # print(self, 'hit /')
                if self.direction == 'down':
                    self.x-=1
                    self.direction = 'left'
                elif self.direction == 'up':
                    self.x+=1
                    self.direction = 'right'
                elif self.direction == 'left':
                    self.y+=1
                    self.direction = 'down'
                elif self.direction == 'right':
                    self.y-=1
                    self.direction = 'up'
                # print(self, 'after /')
            elif data[self.y][self.x] == '-':
                # print(self, 'hit -')
                if self.direction == 'up' or self.direction == 'down':
                    (beam(self.x+1, self.y, 'right', self.number+1).run(data, sol, visited),
                                beam(self.x-1, self.y, 'left', self.number+2).run(data, sol, visited))
                    return
                elif self.direction == 'left':
                    self.x-=1
                elif self.direction == 'right':
                    self.x+=1
                # print(self, 'after -')
            elif data[self.y][self.x] == '|':
                # print(self, 'hit |')
                if self.direction == 'left' or self.direction == 'right':
                    (beam(self.x, self.y-1, 'up', self.number+1).run(data, sol, visited),
                                beam(self.x, self.y+1, 'down', self.number+2).run(data, sol, visited))
                    return
                if self.direction == 'up':
                    self.y-=1
                elif self.direction == 'down':
                    self.y+=1
                # print(self, 'after |')

def compute(data, start_x=0, start_y=0, start_direction='right'):
    
    sol = {j:{i:0 for i in range(110)} for j in range(110)}
    visited = {j:{i:[] for i in range(110)} for j in range(110)}

    beam(start_x, start_y, start_direction).run(data, sol, visited)

    return sum([sol[j][i] for j in range(110) for i in range(110)])

print(compute(data))

# Part 2

counts = {j:{i:0 for i in range(110)} for j in range(110)}

for i in range(110):
    # top row
    counts[0][i] = compute(data, i, 0, 'down')
    # bottom row
    counts[109][i] = compute(data, i, 109, 'up')
    # left column
    counts[i][0] = compute(data, 0, i, 'right')
    # right column
    counts[i][109] = compute(data, 109, i, 'left')

import pandas as pd
print(pd.DataFrame(counts).max().max())