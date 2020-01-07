import os
import pygame
clear = lambda : os.system('cls')

# grids will contain grid objects
grids = []

WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
done = False

class grid:
    def __init__(self,gridHeight = 16,gridWidth = 16,cellSize = 20,cellMargin = 1):
        self.gridHeight : int = gridHeight
        self.gridWidth  : int = gridWidth

        self.cellSize  = cellSize
        self.cellMargin = cellMargin

        self.gridArr = [[0 for x in range(self.gridWidth)] for y in range (self.gridHeight)]

    def displayGrid(self):
        # displays the grid on the console

        count = 0
        space = "  "
        print("+",end="\t")
        for i in range(self.gridWidth):
            # checks if the index number is greater or equal than 10
            # 
            if(i>=10):
                space = " "
            print(i, end = space)

        print()
        for i in self.gridArr:
            print(count,end="\t")
            count+=1
            for j in i:
                if(j):
                    print("*",end = "  ")
                else:
                    print("-",end = "  ")
            print()

    def setLive(self,x,y):
        gridArr[x][y] = 1

    # returns a list of neighbouring coordinates of the selected point
    def neighbourIterator(self,yCoord,xCoord) -> list:
        # Initializes an empty list that contains the neighbour coordinates
        neighbourCoordinates = []
        # Initializes neighbour range, this will be used to iterate through all of the neighbouring cell
        neighbourRange = 3
        yCoord -= 1
        xCoord -= 1

        # Indexes through the neighbouring range, starting from top left (-1,-1 coordinate from origin)
        # and ending at bottom right (+1,+1 coordinate from origin)
        for y in range(neighbourRange):
            for x in range(neighbourRange):
                # This will check if a neighbour is viable (not resulting in IndexError of gridArr). And if it is, it will append it
                # to neighbourCoordinates
                if((yCoord+y<0 or yCoord+y > self.gridHeight-1) or (xCoord+x < 0 or xCoord+x > self.gridWidth-1)):
                    continue
                neighbourCoordinates.append([yCoord+y,xCoord+x])

        # deletes the source coordinate, since that isn't a part of the neighbouring cell
        neighbourCoordinates.remove([yCoord+1,xCoord+1])

        return neighbourCoordinates

    # returns an integer of surrounding live cell
    def neighbourCounter(self,yCoord,xCoord) -> int:
        liveNeighbour = 0
        for neighbour in self.neighbourIterator(yCoord,xCoord):
            if(gridArr[neighbour[0]][neighbour[1]] == True):
                liveNeighbour += 1
        return liveNeighbour

    def nextGeneration(self):
        nextGrid = []
        for y in range(self.gridHeight):
            nextGrid.append([])
            for x in range(self.gridWidth):
                liveNeighbour = self.neighbourCounter(y,x)
                # checks if a live cell has either 2 or 3 live neighbours
                if(self.gridArr[y][x] == True and liveNeighbour in range(2,4)):
                    nextGrid[y].append(1)
                    continue
                elif(self.gridArr[y][x] == False and liveNeighbour == 3):
                    nextGrid[y].append(1)
                    continue
                else:
                    nextGrid[y].append(0)
                    continue
        return nextGrid

    def reader(self,filename):
        # reads a txt file and returns it as a replacement grid
        # also updates the gridWidth and gridHeight

        # checks if the filename is valid, if not, return the previous value
        try:
            txtfile = open(filename+".txt",'r')
        except:
            return self.gridArr

        with open(filename+".txt",'r') as txtfile:

            # reads the file into a list, separated by lines
            lines = txtfile.readlines()
            
            # removes \n from the lines, and creates a separates the elements per line
            # for example ["0,0,0"] will become [0,0,0] with each 0 being a different element instead of one string
            newGrid = [lines[n].replace("\n","").split(',') for n in range(len(lines))]

            # indexes through all the elements in newGrid
            for y in range(len(newGrid)):
                for x in range(len(newGrid[y])):
                    # changes the element inside to be an integer
                    newGrid[y][x] = int(newGrid[y][x])
                    
        self.gridWidth = len(newGrid[0])
        self.gridHeight= len(newGrid)
        return newGrid

    # runs the main loop to add live cells
    def setupGrid(self):
        while True:
            clear()

            print("1. Input live cell")
            print("2. Read from file")
            print("3. Finish")


            option = int(input("Pick option no : "))

            if(option == 1):
                try:
                    a = int(input("Put in col no : "))
                    b = int(input("Put in row no : "))

                    # checks if the input is valid, and not exceeding the array index, border is subtracted by 1 to account for the array
                    assert(isinstance(a,int) and isinstance(b,int))
                    assert((a < 0 or a > self.gridHeight-1) or (b < 0 or b > self.gridWidth-1))
                
                    self.setLive(a,b)
                except AssertionError:
                    print("Invalid Input")
                    input("Press Enter to continue")
                    clear()
                    continue
                
            # prompts the user to insert the name of the file,and replaces the grid with the one read
            elif(option == 2):
                filename = str(input("Insert filename (file must be .txt extension)"))
                self.gridArr = self.reader(filename)

            elif(option == 3):
                break

            displayGrid(self.gridArr,self.gridWidth)
            input("Press Enter to continue")

def initializeNewGrid():
    dataKeywords = ['gridHeight','gridWidth','cellSize','cellMargin']
    gridDatas = {}
    for i in range(len(dataKeywords)):
        dataEntered = False
        while not dataEntered:
            clear()
            print("Enter 0 to for default value")
            try:
                gridData = int(input("Enter " +dataKeywords[i]+ " : "))
                if(gridData != 0):
                    gridDatas[dataKeywords[i]] = gridData
                    dataEntered = True
                else:
                    dataEntered = True
            except:
                continue
    grids.append(grid(**gridDatas))

while True:
    clear()
    print("What would you like to do : ")
    print("1. Add new grid")
    print("2. View grids")

    try:
        option = int(input("Option no : "))
        assert(option <= 2)
        if(option == 1):
            clear()
            initializeNewGrid()
            grids[-1].setupGrid()    
        elif(option == 2 and len(grids) != 0):
            break
        else:
            print("Grid is empty")
            continue
    except:
        print("Invalid input")

# initializes pygame
pygame.init()
clock = pygame.time.Clock()
tick = 0
generation = 0
index = 0


gridArr = grids[index].gridArr
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            index = index+1 if index < len(grids)-1 else 0
            gridArr = grids[index].gridArr
            

    # gets all of the info from the selected grid
    gridWidth = grids[index].gridWidth
    gridHeight = grids[index].gridHeight
    cellSize = grids[index].cellSize
    cellMargin = grids[index].cellMargin
    
    # calculates the size of the screen thats going to be displayed
    screenWidth = gridWidth*(cellSize+cellMargin)+1
    screenHeight = gridHeight*(cellSize+cellMargin)+1
    screen = pygame.display.set_mode((screenWidth,screenHeight))

    # fills the background with black color
    screen.fill(BLACK)

    # draws the block into display
    
    for y in range(gridHeight):
        for x in range(gridWidth):
            if(gridArr[y][x]):
                pygame.draw.rect(screen,GREEN,((cellMargin + cellSize)* x + cellMargin , (cellMargin + cellSize)* y + cellMargin,cellSize,cellSize))
                continue
            pygame.draw.rect(screen,WHITE,((cellMargin + cellSize)* x + cellMargin , (cellMargin + cellSize)* y + cellMargin ,cellSize,cellSize))
    
    # shows the number of generation on the caption
    pygame.display.set_caption('Gen : ' + str(generation))
    
    # for every second, adds the number of generation, and gets the next generation of grid
    tick +=1
    if(tick % 60 == 0):
        tick = 0
        generation += 1
        
        # calculates the next generation of grid and replaces the old one
        gridArr = grids[index].nextGeneration()

    clock.tick(60)
    pygame.display.flip()
pygame.quit()