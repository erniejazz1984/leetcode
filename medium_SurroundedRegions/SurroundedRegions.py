class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
	def solve(self, board):
		lenx = len(board)
		if lenx>0:
			leny= len(board[0])
	
			goodR=[]
			R=[]
			temp = ""
			for i in board[0]:
				if i =="O":
					temp= temp +"a"
				else: 
					temp= temp +i
			temp =""
			for i in board[-1]:
				if i =="O":
					temp= temp +"a"
				else: 
					temp= temp +i
			board[-1]=temp
		
			clean=1
			while clean:
				clean =0
				for x in range(lenx):
					temp=""
					for y in range(leny):
						c=board[x][y]
						if board[x][y]=="O":
							up = board[x][y+1] if (y+1)<leny else -1
							down = board[x][y-1] if (y-1)>=0 else -1
		         				left = board[x+1][y] if (x+1)<lenx else -1
							right = board[x-1][y] if (x-1)>=0 else -1
							border =[up,down,left,right]
							for b in border:
								if b == "a":
									c = "a"
									clean =clean+1
						temp=temp+c
		
					board[x]=temp
		
			for x in range(lenx):
				temp=""
				for y in range(leny):
					c=board[x][y]
					if c =="O":
						c = "X"
					if c =="a":
						c= "O"
					temp=temp+c
		
				board[x]=temp
	
		
s = Solution()
b=["XXX","XOX","XXX"]
s.solve(b)
print b
