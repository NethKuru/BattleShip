from random import randint
class board:

	
	def __init__(self, n):
		self.board = [[' ']*n for x in range(n)]
	
	
	def create_ships(self):
	    for ship in range(5):
	        ship_r, ship_cl=randint(0,7), randint(0,7)
	        while self.board[ship_r][ship_cl] =='X':
	            ship_r, ship_cl = randint(0, 7), randint(0, 7)
	        self.board[ship_r][ship_cl] = 'X'
			
	def create_ship(self, row, colum):
		self.board[row-1][colum-1] = "X"
		
	def if_hit(self, row, column):
		return self.board[row-1][column-1] == "X"
	
	def count_hit_ships(self):
	    count=0
	    for row in self.board:
	        for column in row:
	            if column=='X':
	                count+=1
	    return count
	
	def print_board(self):
	    print(' 1 2 3 4 5 6 7 8')
	    print(' ***************')
	    row_num=1
	    for row in self.board:
	        print("%d|%s|" % (row_num, "|".join(row)))
	        row_num +=1