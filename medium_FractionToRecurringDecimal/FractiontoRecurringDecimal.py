class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        integer = numerator/denominator
	sign = -1 if integer<0 else 1
	numerator = abs(numerator)
	denominator = abs(denominator)
        integer = numerator/denominator
        g = self.gcd(numerator,denominator)
        n = numerator/g
        d = denominator/g
        n = n%d
        b,n2,n5 = self.testFiveTwo(d)
	if n2>n5:
		factor = 5**(n2-n5)
		ten = n2
	else:	
		factor = 2**(n5-n2)
		ten = n5

        if b:
		bz = "%d"%(n*factor)
		zeros = "0"*(ten-len(bz))
		answer = "%d."%(integer)+zeros+bz
		if answer.endswith(".0"):
			answer=answer[:-2]
		if sign <0:
			answer = "-"+answer
		return answer
        else:
		d = d*factor/10**ten
		n = n*factor
		newint = n/d
		n = n - newint*d
		tens,temp = self.tenN1(d)
		print tens,temp
		bz = temp/d*n
		print bz			  
		newint = "%d"%(newint) if newint>0 else ""
		bz = "%d"%(bz)
		pzeros = "0"*(ten-len(newint))
		zeros = "0"*(tens-len(bz))
		answer = "%d."%(integer)+pzeros+newint+"("+zeros+bz+")"
		if answer.endswith(".0"):
			answer=answer[:-2]
		if sign <0:
			answer = "-"+answer
		return answer
        
    def tenN1(self,num):
        n=1
        while True:
            if (10**n-1)%num == 0:
                break
            else:
                n = n+1
        return n,10**n-1 
        
    def gcd(self,x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x
            
    def testFiveTwo(self,x):
        r=0
        n2=0
        while r==0:
            if x%2 == 0:
                x = x /2
                n2= n2+1
            else:
                r = 1
        r=0
        n5=0
        while r==0:
            if x%5 == 0:
                x = x /5
                n5= n5+1
            else:
                r = 1
        
        if x != 1:
            return False,n2,n5
        else:
            return True,n2,n5

s = Solution()
print s.fractionToDecimal(-50,8)
