class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        Lg = -1
        sLg = -1

        # check for digit
        for i in range(len(s)):
            if s[i].isnumeric() and s[i] not in temp:
                int_s = int(s[i])
                temp.append(s[i])
                if int_s > Lg:
                    sLg = Lg
                    Lg = int_s
                elif int_s > sLg and int_s != Lg:
                    sLg = int_s
        return sLg