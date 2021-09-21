# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""
import math


import pygame
from queue import PriorityQueue




class Node():
    """A node class for A* Pathfinding"""



class Pacman:

    def checkMove(self,x,y):
        if x < 0:
            return False
        if x > 9:
            return False
        if y < 0:
            return False
        if y > 9:
            return False
        if grid[x][y] == 3:
            return False
        return True


    def enemyCheck(self,x,y,badx,bady):
        if x == badx and y == bady:
            print("you touched an enemy and died :(")
            return False
        return True

    def WinCheck(self,x,y):
        if x == 8 and y == 8:
            print("You reached the end and won the game")
            return True
        return False


    def enemyMove(self):

        global badx
        global bady

        grid[badx][bady] = 0
        bady = bady - 1
        grid[badx][bady] = 2

    def smartenemyMove(self,x,y):    #start of A* Algorithm

        global badx #use these global variables to keep track of where old enemy position was to erase it
        global bady

        currentNode = queue.get() #pick smallest value off queue
        #the move has been decided
        #clear the queue
        queue.queue.clear()






        enemyx = currentNode[1] #this x value is where we are goind
        enemyy = currentNode[2] #this y value is where we are going

        print("Position enemy travels to ",enemyx,enemyy)



        grid[badx][bady] = 0   #erase old position
        grid[enemyx][enemyy] = 2 #add new position
        badx = enemyx  #update global variables so we can keep track of old position
        bady = enemyy




        # calculate herisitic for each move here, which we will use to pull smallest item off queue
        leftMoveH = p.Heristic(x,y,badx,bady-1)
        upMoveH = p.Heristic(x,y,badx-1,bady)
        rightMoveH = p.Heristic(x,y,badx,bady+1)
        downMoveH = p.Heristic(x, y, badx+1, bady)




        # officially add children to queue after 1 last check to make sure its not a wall
        if grid[badx][bady-1] != 3:
            queue.put((leftMoveH, badx, bady - 1))
        if grid[badx-1][bady] != 3:
            queue.put((upMoveH, badx - 1, bady))
        if grid[badx][bady+1] != 3:
            queue.put((rightMoveH, badx, bady + 1))
        if grid[badx+1][bady] != 3:
            queue.put((downMoveH, badx + 1, bady))








    def  Heristic(self,x,y,badx,bady):
         distance = math.sqrt( ((badx-x)**2)+((bady-y)**2) ) #lets use standard distance formula, which equals square root((x2-x1)^2 + (y2-y1)^2)
         return distance








    # Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
GRAY = (50,50,50)

p = Pacman()

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40

# This sets the margin between each cell
MARGIN = 10

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

x = 0  # x and y will store current position for pacman
y = 0
badx = 7   # badx and bady store current enemy position
bady = 7



# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[0][0] = 1
grid[7][7] = 0
grid[8][8] = 4


queue = PriorityQueue()
h = p.Heristic(x,y,badx,bady)


queue.put((h,badx,bady)) #add starting node, with the heuristic to start, although unnessesary







#create a maze grid for the walls
grid[7][1] = 3
grid[2][2] = 3
grid[2][3] = 3
grid[2][4] = 3
grid[3][4] = 3
grid[5][6] = 3
grid[7][8] = 3




# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [510, 510]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Dontae Moore Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


enemyMove = 26
pygame.time.set_timer(enemyMove, 500)
# -------- Main Program Loop -----------
while not done:
    if not p.enemyCheck(x, y, badx, bady):
        done = True
    if p.WinCheck(x, y):
        done = True
    if pygame.event.get(enemyMove):
        p.smartenemyMove(x,y)


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                if p.checkMove(x,y-1):  # check to see if new position is possible
                    grid[x][y] = 0      # erase old position
                    y = y - 1
                    grid[x][y] = 1      # Update grid to new position
            if event.key == pygame.K_RIGHT:
                if p.checkMove(x, y + 1):
                    grid[x][y] = 0
                    y = y+1
                    grid[x][y] = 1
            if event.key == pygame.K_UP:
                if p.checkMove(x-1, y):
                    grid[x][y] = 0
                    x = x - 1
                    grid[x][y] = 1
            if event.key == pygame.K_DOWN:
                if p.checkMove(x+1, y):
                    grid[x][y] = 0
                    x = x + 1
                    grid[x][y] = 1


        # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = YELLOW
            if grid[row][column] == 2:
                color = RED
            if grid[row][column] == 3:
                    color = GRAY
            if grid[row][column] == 4:
                    color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

