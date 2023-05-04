import turtle

PART_OF_PATH = "*"
TRIED = "."
WALL = "x"
DEAD_END = "-"


class Maze:

    def __init__(self, maze_file):
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.start_col = 0
        self.start_row = 0
        self.maze = []
        cols = 0
        rows = 0
        maze_file = open(maze_file, "r")
        for row in maze_file:
            row_list = []
            loop_col = 0
            for ch in row:
                if ch != '\n':
                    row_list.append(ch)
                if ch == "S":
                    self.start_col = loop_col
                    self.start_row = rows
                loop_col += 1
            rows += 1
            self.maze.append(row_list)
            cols = len(row_list)
        self.cols_in_maze = cols  # max number of cols in file
        self.rows_in_maze = rows  # max number of rows in file
        self.x_translate = -cols / 2
        self.y_translate = rows / 2
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(
            -(cols - 1) / 2 - 1,
            -(rows - 1) / 2 - 1,
            (cols - 1) / 2 + 1,
            (rows - 1) / 2 + 1,
        )

    def draw_maze(self):
        self.wn.tracer(0)  # draw the walls immediately
        for y in range(self.rows_in_maze):
            for x in range(self.cols_in_maze):
                if self.maze[y][x] == WALL:
                    coord_x = x + self.x_translate
                    coord_y = -y + self.y_translate
                    self.draw_centered_box(coord_x, coord_y, "orange")
        self.t.up()
        self.t.goto(self.start_col + self.x_translate, -self.start_row + self.y_translate)
        self.t.color("black", "blue")

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color("black", color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def move_turtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(x + self.x_translate, -y + self.y_translate))
        self.t.goto(x + self.x_translate, -y + self.y_translate)

    def update_position(self, row, col, val=None):
        self.move_turtle(col, row)
        if val:
            self.maze[row][col] = val
        if val == PART_OF_PATH:
            color = "green"
        elif val == WALL:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None
        if color:
            self.drop_bread_crumb(color)
        self.wn.tracer(1)  # slow down turtle. comment out this line to make turtle fast
        self.wn.update()  # show the movement of the turtle

    def drop_bread_crumb(self, color):
        self.t.dot(10, color)

    def is_exit(self, row, col):
        # If the given coordinate is on any of the 4 edges of the maze, we've found the exit
        if (
                row == 0
                or row == self.rows_in_maze - 1
                or col == 0
                or col == self.cols_in_maze - 1
        ):
            return True
        else:
            return False

    def __getitem__(self, idx):
        return self.maze[idx]


def search_from(maze, start_row, start_column):
    # Base case 1: If turtle ran into the wall, return False.
    if maze[start_row][start_column] == WALL:
        return False
    # Base case 2: If turtle lands on an explored square, return False.
    if (
            maze[start_row][start_column] == TRIED
            or maze[start_row][start_column] == DEAD_END
    ):
        return False
    # Base case 3: If turtle finds an exit, update maze and return true.
    if maze.is_exit(start_row, start_column):
        maze.update_position(start_row, start_column, PART_OF_PATH)
        return True

    # If none of the 3 cases apply, we have landed on an open square.
    # Mark the square as "TRIED", then, run the current parent
    # function RECURSIVELY with different arguments to
    # make turtle do down the 4 adjacent directions and see if any of them
    # will achieve the #3 exit base case.
    maze.update_position(start_row, start_column, TRIED)
    exit_found = (
            search_from(maze, start_row - 1, start_column)  # North
            or search_from(maze, start_row + 1, start_column)  # South
            or search_from(maze, start_row, start_column - 1)  # West
            or search_from(maze, start_row, start_column + 1)  # East
    )
    if exit_found:
        maze.update_position(start_row, start_column, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_column, DEAD_END)
    return exit_found


maze1 = Maze("maze.txt")
maze1.draw_maze()
search_from(maze1, maze1.start_row, maze1.start_col)
maze1.wn.exitonclick()
