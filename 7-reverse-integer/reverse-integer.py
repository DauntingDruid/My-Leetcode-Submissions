class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # Variables
        s = list(str(x))
        i = len(s) - 1
        j = 0
        flag = 0

        # Check Negative
        if s[0] == '-':
            j = 1
            flag = 1

        # Reverse String
        while i >= ((len(s) - 1)//2) + 1 and j <= (len(s) - 1)//2:
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            i -= 1 
            j += 1

        # Constraint Check
        res = int("".join(s))

        if -2**31 <= res and res <= (2**31 - 1) :
            return res
        else:
            return 0



        