import random
player1_score = 0
player2_score = 0
print("Welcome to to the board game, make your choice")
print("The game strategy is to select a matching pair of tiles")
print("The player who makes the most number of matches wins the game")
print("Here is the board as at the present")
print("Let's begin the game, the first player should begin by picking indices where matching values are found")

matched_letters = []
matched_indices = []

player1 = True
player2 = False
def make_board():
    tiles = ['A','B','C','D','E','F','G','H','A','B','C','D','E','F','G','H']
    random.shuffle(tiles)
    return tiles
def show_board(board):
    string = ""
    for value in board:
        if value in matched_letters:
            string+= value
        else:
            string += "_"
    return string
def is_match(a,b):
    if a == b:
        return True
    else:
        return False

board = make_board()
print(board)
while True:
    if len(matched_indices)>= len(board):
        print("Game over, Thank you")
        break
    try:
        first_pick = int(input("Please enter your first index of pick"))
        second_pick = int(input("Please enter your second index of pick"))
    except:
        print("You're entry is invalid please start off again")
        continue
    if is_match(board[first_pick],board[second_pick]):
        if (first_pick in matched_indices):
            print("The indices had already been matched")
            print('Please select another set')
        if player1:
            player1_score += 1
        elif player2:
            player2_score += 1
        matched_letters.append(board[first_pick])
        matched_indices.append(first_pick)
        matched_indices.append(second_pick)
        print("You have won yourself a turn by picking the right pair")
        print(f"Here is the board as at the moment: {show_board(board)}")
        continue
    else:
        print("No, you sucked passed the turn to the next player")
        if player1:
            player1 = False
            player2 = True
        else:
            player1 = True
            player2 = False
        print("Let the next player begin")
        print(f"Here is the board as at the moment: {show_board(board)}")
    
if player1_score == player2_score:
    print("There is a tie")
elif player1_score > player2_score:
    print("The first player wins")
else:
    print("The second player wins")