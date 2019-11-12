from mediaire_code_challenge import Board, Player
import numpy as np

# i keep the numbers below 10 to decrease waiting time for you
# there is not any memory overflow problem supposed to happen
# else an exception would be raised
amount_colors = [0, 1, -1, 5, 3, 3 + 2j, False, "color"]
dimensions = [0, 1, -1, 7, 5 + 4j, True, "size"]
test_player_board = Board(4,3)

def test_init_board():
    for color in amount_colors:
        for dim in dimensions:
            test_board = Board(dim, color)
            print("Board with test dimension "+str(dim)+" and amount of colors "+str(color)+" is:")
            #print("Board with test dimension %d and amount of colors %d is:" % (dim, color))
            if type(test_board) is np.array:
                print("Board initialized")
            else:
                print("No Board initialized")

            print("\n \n")
    
def test_init_player(test_player_board):
    player = Player(test_player_board)
    print(player.current_color)
    print(player.board.board[0,0])

def test_make_move():
    player = Player(test_player_board)
    player.make_move()
    print(player.converted_fields)
    print(player.counter_hash_map)
    print(player.board.board)

test_init_board()
#test_init_player(test_player_board)
#test_make_move()
