class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        lenx = len(board)
        if lenx>0:
            leny= len(board[0])

        goodR=[]
        R=[]
        for x in range(lenx):
            for y in range(leny):
                if board[x][y] =="O":
                    up = board[x][y+1] if (y+1)<leny else -1
                    down = board[x][y-1] if (y-1)>=0 else -1
                    left = board[x+1][y] if (x+1)<lenx else -1
                    right = board[x-1][y] if (x-1)>=0 else -1
                    border =[up,down,left,right]
                    region = None
                    for b in border:
                        if b in R:
                            region =b 
                    if not region:
                        region = len(R)+1
                        R.append(region)
                    
		    board[x] =board[x][0:y]+str(region)+board[x][y+1:]
                    
                    newB=[]
                    for b in border:
                        if b == -1:
                            goodR.append(region)
                        if b =="O":
                            newB.append(region)
                        else:
                            newB.append(b)
#                    if y+1<leny:
#                        board[x][y+1] = newB[0]
#                    if y-1>0:
#                        board[x][y-1] = newB[1]
#                    if x+1<lenx:
#                        board[x+1][y] = newB[2]
#                    if x-1>0:
#                        board[x-1][y] = newB[3]
                            
        for x in range(lenx):
            for y in range(leny):
                if board[x][y] !="X":
                    if int(board[x][y]) in goodR:
                        board[x] =board[x][0:y]+"O"+board[x][y+1:]
                    else:
                        board[x] =board[x][0:y]+"X"+board[x][y+1:]
s = Solution()
b=["XXX","XOX","XXX"]
#b=["O"]
s.solve(b)
print b
