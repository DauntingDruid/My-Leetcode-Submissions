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

        # Swap characters in list
        while i >= ((len(s) - 1)//2) + 1 and j <= (len(s) - 1)//2:
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            i -= 1 
            j += 1

        # Join characters in list and converting to int
        res = int("".join(s))

        # Constraint check
        if -2**31 <= res and res <= (2**31 - 1) :
            return res
        else:
            return 0



        