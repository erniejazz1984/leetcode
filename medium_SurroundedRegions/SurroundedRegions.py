class Solution0:
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
	
		
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
	def constructMatrix(self,board):
		matrix = []
		for n,i in enumerate(board):
			matrix.append([])
			for n2,j in enumerate(i):
				ele = 0 if j =="X" else 1
				matrix[n].append(ele)

		return matrix

	def reconstruct(self,matrix,board):
		for i in range(len(matrix)):
			temp = ""
			for j in matrix[i]:
				ele = "X" if j ==0 else "O"
				temp = temp +ele
			board[i] = temp

	def solve(self, board):
		matrix= self.constructMatrix(board)
		#exit()
		lenx = len(matrix)
		if lenx>0:
			leny= len(matrix[0])
		
			clean=1
			while clean:
				clean =0
				for x in range(lenx):
					for y in range(leny):
						c=matrix[x][y]
						if matrix[x][y]==1:
							up = matrix[x][y+1] if (y+1)<leny else -1
							down = matrix[x][y-1] if (y-1)>=0 else -1
		         				left = matrix[x+1][y] if (x+1)<lenx else -1
							right = matrix[x-1][y] if (x-1)>=0 else -1
							border =[down,right,left,up]
							for b in border:
								if b == -1:
									matrix[x][y] = -1
									clean =clean+1
		
			print matrix
			for x in range(lenx):
				for y in range(leny):
					c=matrix[x][y]
					if c ==1:
						matrix[x][y]=0
					if c ==-1:
						matrix[x][y]=1

		self.reconstruct(matrix,board)


s = Solution()
b=["XXX","XOX","XXX"]
b=["XOX","OXO","XOX"]
print b
s.solve(b)
print b
