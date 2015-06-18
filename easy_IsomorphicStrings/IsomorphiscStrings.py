class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s)==0:
            return True
        dic ={}
        for a,b in zip(s,t):
            if a in dic.keys():
                if dic[a] != b:
                    return False
            else:
		if b in dic.values():
			return False
                dic[a] = b
        return True

s =Solution()
print s.isIsomorphic("ab","aa")
