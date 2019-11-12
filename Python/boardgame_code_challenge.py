import numpy as np
import pandas as pd

# down the road...
# apply the result of hashmap to converted
# iterate through the moves by the game method
# set counters in game method
# i am very sorry.. the problem is very interesting and I would have liked to solve it.
# due to illness I had to interupt a couple of times though :(
# also there might have been more tests.
# did not get to it 

# problem: implement a game of nxn Board, fields colored in k different colors
# each move a color is chosen, so the path from left upper field and every adjacent field
# with the same color will be colored that way
# color all fields unicolor in the least possible moves

class Board:

    def __init__(self, board_dimension, amount_colors):
        self.init_board_dimension(board_dimension)
        self.init_amount_colors(amount_colors)
        self.init_board()
        
    # init the board dimension and check for value errors
    def init_board_dimension(self, board_dimension):
        try:
            self.board_dimension = board_dimension

            # if the input is not an int raise an exception
            if not isinstance(board_dimension, int):
                raise ValueError("Board size needs to be defined as a positive integral number greater 1")

            elif board_dimension <= 1:
                raise ValueError("Board needs to have positive dimensions greater 1")
            
        except ValueError as e:
            print(e)

    # init the amout of colors and check for value errors
    def init_amount_colors(self, amount_colors):
        try: 
            self.amount_colors = amount_colors
            
            # if the input is not an int raise an exception
            if not isinstance(amount_colors, int):
                raise ValueError("Please define an amount of colors as an integral number greater 1")
                
            # if the input is less then 2 raise an exception
            elif amount_colors <= 1:
                raise ValueError("Would be fun to play with at least two colors, wouldnt it?")
        except ValueError as e:
            print(e)            

    def init_board(self):
        try:
            df = pd.DataFrame(np.random.randint(1, self.amount_colors, (self.board_dimension, self.board_dimension)))
            self.board = df.to_numpy()
        except Exception as e:
            print(e)


class Player():

    def __init__(self, board):

        self.move_counter = 0
        self.board = board
        self.init_current_color()
        
        # hash map in order to count fields for each color for each move
        # also keeps track of fields to be converted in the fashion of:
        # {[color#] = [(row_coordinate, column_coordinate), (row_coordinate, column_coordinate),...], ...}
        self.init_counter_hash_map()
        
        self.current_converted_fields = 1
        self.init_max_converted_fields()
        
        # list of fields already converted
        self.init_converted_fields()
        
    def init_converted_fields(self):
        #self.converted_fields = np.zeros(self.board.board_dimension, self.board.board_dimension)
        #self.converted_fields[0,0] = 1
        self.converted_fields = [(0,0)]
        self.check_initial_converted_size()

    def init_current_color(self):
        self.current_color = self.board.board[0,0]

    def init_max_converted_fields(self):
        self.max_converted_fields = self.board.board_dimension**2
    
    def set_current_color(self, color):
        self.current_color = color

    def init_counter_hash_map(self):
        self.counter_hash_map = {self.current_color : [(0,0)]}
        for color in range(self.board.amount_colors):
            self.counter_hash_map[color] = list()

    # intialy there might be more fields adjacent to (0,0) converted already    
    def check_initial_converted_size(self):
        converted = self.converted_fields
        
        for field in converted:
            
            current_x = field[1]
            current_y = field[0]
            # look south
            if current_y+1<self.board.board_dimension and self.board.board[current_y+1, current_x] == self.current_color:
                
                # only append those not in list
                if (current_y+1,current_x) not in self.converted_fields: 
                    converted.append((current_y+1,current_x))
                    self.converted_fields.append((current_y+1,current_x))
            # look north
            if current_y-1>0 and self.board.board[current_y-1, current_x] == self.current_color:
                
                # only append those not in list
                if (current_y-1,current_x) not in self.converted_fields:
                    converted.append((current_y-1,current_x))
                    self.converted_fields.append((current_y-1,current_x))
            #look east
            if current_x+1<self.board.board_dimension and self.board.board[current_y, current_x+1] == self.current_color:
                
                # only append those not in list
                if (current_y,current_x+1) not in self.converted_fields:
                    converted.append((current_y,current_x+1))
                    self.converted_fields.append((current_y,current_x+1))
            #look east
            if current_x-1>0 and self.board.board[current_y, current_x-1] == self.current_color:
                
                # only append those not in list
                if (current_y,current_x-1) not in self.converted_fields:  
                    converted.append((current_y,current_x-1))
                    self.converted_fields.append((current_y,current_x-1))
            
            

    # count colors as in storing tuples of coordinates for each color adjacent to current playing field
    # except the current color of origin
    # only check the converted fields beginning at max values for each row and column having color of origin 
    def make_move(self):
            
        # fields are tuples of coordinates (y,x)
        # check all fields already converted
        for field in self.converted_fields:
            current_x = field[1]
            current_y = field[0]
                
            # look at surrounding fields for other colors and store them if not the same as current
            # look north
            if current_y-1>0 and self.board.board[current_y-1, current_x] != self.current_color and (current_y-1,current_x) not in self.counter_hash_map[self.board.board[current_y-1, current_x]]:
                self.counter_hash_map[self.board.board[current_y-1, current_x]].append((current_y-1,current_x))
                
            # look east
            if current_x+1<self.board.board_dimension and self.board.board[current_y, current_x+1] != self.current_color and (current_y, current_x+1) not in self.counter_hash_map[self.board.board[current_y, current_x+1]]:
                self.counter_hash_map[self.board.board[current_y, current_x+1]].append((current_y,current_x+1))
                
            # look south
            if current_y+1<self.board.board_dimension and self.board.board[current_y+1, current_x] != self.current_color and (current_y+1,current_x) not in self.counter_hash_map[self.board.board[current_y, current_x]]:
                self.counter_hash_map[self.board.board[current_y, current_x]].append((current_y+1,current_x))

            # look west
            if current_x-1>0 and self.board.board[current_y, current_x-1] != self.current_color and (current_y,current_x-1) not in self.counter_hash_map[self.board.board[current_y, current_x]]:
                self.counter_hash_map[self.board.board[current_y, current_x]].append((current_y,current_x-1))



    # should be written as class eventually
    def play_game(self):

        # as long as not everything has been converted
        while self.converted_fields < self.max_converted_fields:
            #put in some player interaction here
            self.make_move()


