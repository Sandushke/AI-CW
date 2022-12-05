import random

print("--- 6 x 6 Maze---")

# TASK 1
def create_maze():
    # Create a 2D array for the maze
    maze_size = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]

    # Set a start goal point between the last two columns
    global start_X, start_Y
    start_X = random.randint(0, 5)
    start_Y = random.randint(0, 1)

    # Setting the start goal point to 2
    maze_size[start_X][start_Y] = 2

    # Set an end goal point between the 1st two columns
    global end_X, end_Y
    end_X = random.randint(0, 5)
    end_Y = random.randint(4, 5)

    # Set the end goal point as 4
    maze_size[end_X][end_Y] = 4

    # Create a barrier to the maize
    barrier = 0
    while barrier < 4:
        barrier_X = random.randint(0, 5)
        barrier_Y = random.randint(0, 5)

        # Check if barrier falls on the index values of start and end goal
        barrier_point = maze_size[barrier_X][barrier_Y]
        if barrier_point == 2 or barrier_point == 4 or barrier_point == 1:
            barrier = barrier
            continue

        # Place 4 barrier nodes in the maze
        else:
            maze_size[barrier_X][barrier_Y] = 1
            barrier += 1

    # Print the 2D array one below the other
    for i in maze_size:
        for j in i:
            print(j, end=" ")
        print()

# Call the function maze
create_maze()


# TASK 2
# Create a stack
def create_stack():
    stack = []
    return stack

# Check whether the stack is empty
def isEmpty(stack):
    return len(stack) == 0

# Add a value to the stack
def push_stack(stack, number):
    stack.append(number)

# Remove a value in the stack
def pop_stack(stack):
    if isEmpty(stack):
        return "The stack is empty"

    return pop_stack()

stack = create_stack()

print()
print("DFS ALGORITHM ")

# Using DFS algorithm
def DFS(start_row, start_col, end_row, end_col):
    xcord = start_row
    ycord = start_col
    start = {xcord: ycord}
    explored_node = {xcord: ycord}

    # front_node = {xcord, ycord - 1}
    dfs_path = []   #pop the dfs path to the stack
    dfs_path.append(start)
    push_stack(stack, str(start))

    #Initializing the cell values
    top_node = [xcord-1][ycord]
    left_node = [xcord][ycord-1]

    right_node=-1
    if (ycord==-1):
        right_node = [xcord][ycord+1]

    bottom_node=-1
    if(xcord<2):
        bottom_node = [xcord+1][ycord]


    value = 0
    while value < 36:
        if(left_node == 0 or left_node == 4) & (ycord!=0):
            if([xcord-1][ycord] == 4):
                print("DFS path found 1")
                print("Start Node: " + str(xcord), str(ycord))
                print("Goal Node: " + str(end_row), str(end_col))
                xcord = xcord-1
                ycord = ycord
                explored_node = {xcord: ycord}
                dfs_path.append(explored_node)
                break
            [xcord-1][ycord] = -1
            xcord = xcord-1
            ycord = ycord
            explored_node = {xcord: ycord}
            dfs_path.append(explored_node)
            top_node = [xcord-1][ycord]
            left_node = [xcord][ycord-1]
            if (xcord < -1):
                right_node = [xcord + 1][ycord]
            if (ycord < -1):
                bottom_node = [xcord][ycord + 1]
            value +=1

        elif(top_node == 0 or top_node == 4) & (xcord!=0):
            if([xcord][ycord-1] == 4):
                print("DFS path found 2")
                print("Start Node: " + str(xcord), str(ycord))
                print("Goal Node: " + str(end_row), str(end_col))
                xcord = xcord
                ycord = ycord-1
                explored_node = {xcord: ycord}
                dfs_path.append(explored_node)
                break
            [xcord][ycord-1] = -1
            xcord = xcord
            ycord = ycord-1
            explored_node = {xcord: ycord}
            dfs_path.append(explored_node)
            top_node = 4
            left_node = [xcord - 1][ycord]
            if (xcord < -1):
                right_node = [xcord + 1][ycord]
            if (ycord < -1):
                bottom_node = [xcord][ycord + 1]
            value +=1

        elif(bottom_node == 0 or bottom_node == 4) & (ycord!=2):
            if([xcord][ycord+1] == 4):
                print("DFS path found 3")
                print("Start Node: " + str(xcord), str(ycord))
                print("Goal Node: " + str(end_row), str(end_col))
                xcord = xcord
                ycord = ycord+1
                explored_node = {xcord: ycord}
                dfs_path.append(explored_node)
                break
            [xcord][ycord+1] = -1
            xcord = xcord
            ycord = ycord + 1
            explored_node = {xcord: ycord}
            dfs_path.append(explored_node)
            top_node = [xcord][ycord - 1]
            left_node = [xcord - 1][ycord]
            if (xcord < -1):
                right_node = [xcord + 1][ycord]
            if (ycord < -1):
                bottom_node = [xcord][ycord + 1]
            value +=1

        elif(right_node == 0 or right_node == 4) & (ycord!=2):
            if([xcord+1][ycord] == 4):
                print("DFS path found 4")
                print("Start Node: " + str(xcord), str(ycord))
                print("Goal Node: " + str(end_row), str(end_col))
                xcord = xcord+1
                ycord = ycord
                explored_node = {xcord: ycord}
                dfs_path.append(explored_node)
                break
            [xcord+1][ycord] = -1
            xcord = xcord+1
            ycord = ycord
            explored_node = {xcord: ycord}
            dfs_path.append(explored_node)
            top_node = [xcord][ycord - 1]
            left_node = [xcord - 1][ycord]
            if (xcord < -1):
                right_node = [xcord + 1][ycord]
            if (ycord < -1):
                bottom_node = [xcord][ycord + 1]
            value +=1

        else:
            print("DFS path not found")
            break
    # explored_node = {xcord: ycord}
    # dfs_path.append(explored_node)
    # print(dfs_path)

DFS(start_X,start_Y, end_X, end_Y)


#Finding the heuristic costs
def getHeuristicCost(end_X, end_Y):
    a = 0
    GX = end_X
    GY = end_Y

    print("")
    for i in range(a, 6):
        b = 0
        for j in range(0, 6):
            heuristicCost = max(abs(a - GX), abs(b - GY))
            print("Heuristic cost of (" + str(a) + "," + str(b) + "): " + str(heuristicCost))
            b +=1
        a+=1

getHeuristicCost(end_X, end_Y)



