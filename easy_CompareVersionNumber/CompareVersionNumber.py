class Solution:

    # @param {string} version1

    # @param {string} version2

    # @return {integer}

    def compareVersion(self, version1, version2):

        v1 = version1.split(".")
        v2 = version2.split(".")
        self.matchV(v1,v2)
        for i ,j in zip(v1,v2):
            if int(i)>int(j):
                return 1
            elif int(j)>int(i):
                return -1
        return 0

    def matchV(self,v1,v2):
        l1 = len(v1)
        l2 = len(v2)
        if l1>l2:
            for i in range(l1-l2):
                v2.append("0")
        else:
            for i in range(l2-l1):
                v1.append("0")
        for i in range(min(l1,l2)):
            ll1 = len(v1[i])
            ll2 = len(v2[i])
            zeros = "0"*abs(ll1-ll2)
            if ll1 > ll2:
                v2[i] = zeros+v2[i]
            else:
                v1[i] = zeros+v1[i]

a = Solution()
print a.compareVersion("0","1")
