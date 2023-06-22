from board import *
from random import randint

Comp_Board = board(8)
Player_Board = board(8)
hit_board = board(8)
Comp_Board.create_ships()
Comp_Board.print_board()
win_player = 0
win_comp = 0
for x in range(5):
	a= input("Enter row and column of ships(row-column): ")
	Player_Board.create_ship(int(a[0:a.index("-")]), int(a[a.index("-")+1:len(a)]))
print("Your Board:")
Player_Board.print_board()
while win_player <=5 or win_comp<=5:
	b = input("Enter row and column to hit: ")
	if Comp_Board.if_hit(int(b[0:b.index("-")]), int(b[b.index("-")+1:len(b)])):
		hit_board.board[int(b[0:b.index("-")])-1][int(b[b.index("-")+1:len(b)])-1] = "X"
		print("YOU HIT!")
		win_player+=1
	else:
		hit_board.board[int(b[0:b.index("-")])-1][int(b[b.index("-")+1:len(b)])-1] = "-"
		print("YOU MISSED!")
	row_C = randint(1,8)
	column_C = randint(1,8)
	print("Computer choses to hit" , row_C, "-", column_C)
	if Player_Board.if_hit(row_C, column_C):
		win_comp+=1
		print("Computer HIT!")
	else:
		print("Computer MISSED!")
	print("_______________________________________")
	hit_board.print_board()
if win_player ==5:
	print("YOU WINS!!!")
else:
	print("YOU LOSE")

		
	