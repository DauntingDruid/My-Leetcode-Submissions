class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        xlen =len(str(x)) 
        i=0
        j=len(str(x))-1

        while i <= xlen/2 and j >= xlen/2:
            if s[i] is not s[j]:
                return False
            else: 
                i = i + 1
                j = j - 1
        return True
                    
        
        