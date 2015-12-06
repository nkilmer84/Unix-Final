Initial Commit test
# -*- coding: utf-8 -*-
directions =  "This game is like regular tic-tac-toe but with a twist. Each position inside the tic-tac-toe board is another tic-tac-toe board, so in order to win, you have to win 3 boards in a row. There’s more to it than that though. When you play on a board, the position on the inner board that you play on, corresponds to the board that the other person must play on next. Thereby making the game much more strategic! On top of this, you can send someone to a board that has already been one, but once it has been one it cannot be taken. Another catch is if you send someone to a board that is full, they can then choose to play on any board they want." 

print directions
print ""
print "This is a two player game. Player one will play first by etnering which board they'd like followed by which location in that board that they would like. Afterwards each player will simply choose the location they would like within the board they must play in. The boards/locations are represented by a 2 character position(this is what the user must enter to play). Those positions are as following UL(Upper Left), UM(Upper Middle), UR(Upper Right), ML(Middle Left), MM(middle), MR(middle right), LL(lower left), LM(Lower mid), LR(lower right)"

print ""
print "As an example, player one could enter UL LL to play in the upper left board, lower left position in that board. Then player 2 could simply enter MR to play in the middle right and the game would go from there."

print ""

input = raw_input("Once you understand the directions Press Enter to Play")

board = []
for i in range(0,9):
	temp = []
	for j in range(0,9):
		temp.append("  ")
		#temp.append(str(i) +str(j))
	board.append(temp)

wins = []
for i in range(0,9):
	wins.append(0)


print ""
print ""
print ""


#start function definitions


def printBoard():
	print board[0][0] + "|" + board[0][1] +"|" + board[0][2] + "   ||   " + board[1][0] + "|" + board[1][1] + "|" + board[1][2] + "   ||   " + board[2][0] + "|" + board[2][1] + "|" + board[2][2]
	print "--------   ||   --------   ||   --------"
	print board[0][3] + "|" + board[0][4] +"|" + board[0][5] + "   ||   " + board[1][3] + "|" + board[1][4] + "|" + board[1][5] + "   ||   " + board[2][3] + "|" + board[2][4] + "|" + board[2][5]
	print "--------   ||   --------   ||   --------"
	print board[0][6] + "|" + board[0][7] +"|" + board[0][8] + "   ||   " + board[1][6] + "|" + board[1][7] + "|" + board[1][8] + "   ||   " + board[2][6] + "|" + board[2][7] + "|" + board[2][8]
	print "________________________________________"
	print board[3][0] + "|" + board[3][1] +"|" + board[3][2] + "   ||   " + board[4][0] + "|" + board[4][1] + "|" + board[4][2] + "   ||   " + board[5][0] + "|" + board[5][1] + "|" + board[5][2]
	print "--------   ||   --------   ||   --------"
	print board[3][3] + "|" + board[3][4] +"|" + board[3][5] + "   ||   " + board[4][3] + "|" + board[4][4] + "|" + board[4][5] + "   ||   " + board[5][3] + "|" + board[5][4] + "|" + board[5][5]
	print "--------   ||   --------   ||   --------"
	print board[3][6] + "|" + board[3][7] +"|" + board[3][8] + "   ||   " + board[4][6] + "|" + board[4][7] + "|" + board[4][8] + "   ||   " + board[5][6] + "|" + board[5][7] + "|" + board[5][8]
	print "________________________________________"
	print board[6][0] + "|" + board[6][1] +"|" + board[6][2] + "   ||   " + board[7][0] + "|" + board[7][1] + "|" + board[7][2] + "   ||   " + board[8][0] + "|" + board[8][1] + "|" + board[8][2]
	print "--------   ||   --------   ||   --------"
	print board[6][3] + "|" + board[6][4] +"|" + board[6][5] + "   ||   " + board[7][3] + "|" + board[7][4] + "|" + board[7][5] + "   ||   " + board[8][3] + "|" + board[8][4] + "|" + board[8][5]
	print "--------   ||   --------   ||   --------"
	print board[6][6] + "|" + board[6][7] +"|" + board[6][8] + "   ||   " + board[7][6] + "|" + board[7][7] + "|" + board[7][8] + "   ||   " + board[8][6] + "|" + board[8][7] + "|" + board[8][8]
	print ""
	print ""


def switchPlayer(test):
	if(test == 1):
		return 2
	if(test == 2):
		return 1

			
def grabPosition(test):
	if(test == "UL"):
		return 0
	if(test == "UM"):
		return 1
	if(test == "UR"):
		return 2
	if(test == "ML"):
		return 3
	if test == "MM":
		return 4
	if test == "MR":
		return 5
	if test == "LL":
		return 6
	if test == "LM":
		return 7
	if test == "LR":
		return 8
def testSmallBoardWon(pos, player):
	mid = board[pos][4]
	if(wins[pos] !=0):
		return;
	if(board[pos][4] != "  "):
		if(mid == board[pos][1] and mid == board[pos][7]):
			wins[pos] = player
			if(player==1):
				board[pos][4] = "XX"
				board[pos][1] = "XX"
				board[pos][7] = "XX"
			else:
				board[pos][4] = "OO"
				board[pos][1] = "OO"
				board[pos][7] = "OO"
			return; 
		if(mid == board[pos][3] and mid == board[pos][5]): 
			wins[pos] = player
			if(player==1):
				board[pos][4] = "XX"
				board[pos][3] = "XX"
				board[pos][5] = "XX"
			else:
				board[pos][4] = "OO"
				board[pos][3] = "OO"
				board[pos][5] = "OO"
			return;
		if(mid == board[pos][0] and mid == board[pos][8]): 
			wins[pos] = player
			if(player==1):
				board[pos][4] = "XX"
				board[pos][0] = "XX"
				board[pos][8] = "XX"
			else:
				board[pos][4] = "OO"
				board[pos][0] = "OO"
				board[pos][8] = "OO"
			return;
		if(mid == board[pos][2] and mid == board[pos][6]):
			wins[pos] = player
			if(player==1):
				board[pos][4] = "XX"
				board[pos][2] = "XX"
				board[pos][6] = "XX"
			else:
				board[pos][4] = "OO"
				board[pos][2] = "OO"
				board[pos][6] = "OO"
			return;
	if(board[pos][1] != "  " and board[pos][1] == board[pos][0] and board[pos][1] == board[pos][2]):
		wins[pos] = player
		if(player==1):
			board[pos][1] = "XX"
			board[pos][0] = "XX"
			board[pos][2] = "XX"
		else:
			board[pos][1] = "OO"
			board[pos][0] = "OO"
			board[pos][2] = "OO"
		return;
	if(board[pos][7] != "  " and board[pos][7] == board[pos][8] and board[pos][7] == board[pos][6]):
		wins[pos] = player
		if(player==1):
			board[pos][7] = "XX"
			board[pos][8] = "XX"
			board[pos][6] = "XX"
		else:
			board[pos][7] = "OO"
			board[pos][8] = "OO"
			board[pos][6] = "OO"
		return;
	if(board[pos][3] != "  " and board[pos][3] == board[pos][0] and board[pos][3] == board[pos][6]):
		wins[pos] = player
		if(player==1):
			board[pos][3] = "XX"
			board[pos][0] = "XX"
			board[pos][6] = "XX"
		else:
			board[pos][3] = "OO"
			board[pos][0] = "OO"
			board[pos][6] = "OO"
		return;
	if(board[pos][5] != "  " and board[pos][5] == board[pos][2] and board[pos][5] == board[pos][8]):
		wins[pos] = player
		if(player==1):
			board[pos][2] = "XX"
			board[pos][8] = "XX"
			board[pos][5] = "XX"
		else:
			board[pos][2] = "OO"
			board[pos][8] = "OO"
			board[pos][5] = "OO"
		return;

	
	



#end function definitions




printBoard()

player = 1
input = raw_input("Player one make the first move (board followed by a space followed by position)")
boardPos = input[0:2]
pos = grabPosition(boardPos)
location = input[3:5]
loc = grabPosition(location)
board[pos][loc] = "X "
pos = loc;
printBoard()
player = switchPlayer(player)

while(1):
	global pos
	global location
	validInput = 1;
	if(player ==1):
		input = raw_input("Player 1 make your move in the " + location + " board:  ")
		loc = grabPosition(input)
		if(board[pos][loc] == "  "):
			location = input
			board[pos][loc] = "X "
		else:
			validInput = 0;
			print("Location is already taken")
			
	if(player == 2):
		input = raw_input("Player 2 make your move in the " + location + " board:  ")
		loc = grabPosition(input)
		if(board[pos][loc] == "  "):
			location = input
			board[pos][loc] = "O "
		else:
			validInput = 0;
			print("Location is already taken")
	if(validInput):
		testSmallBoardWon(pos, player)
		tempPos = pos;
		pos = loc
		printBoard()
		if(wins[tempPos]!=0):
			print("Player " + str(player) + " wins the board")
		player = switchPlayer(player)
	




