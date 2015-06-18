class Solution:

    # @param {string} s

    # @return {string}

    def shortestPalindrome(self, s):

        good=0

        for i in range(len(s)/2+1):

            temp = s[0:(i*2+1)]

            if self.check(temp):

               good = i   

        

        

    def 

        
