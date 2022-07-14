def reverseString(self, s: List[str]) -> None:
        '''
        my answer
        '''
        i = 0
        l = len(s)
        while i < l:
            s[i], s[l-1] = s[l-1], s[i]
            i += 1
            l -= 1

        '''
        other's solution
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
        '''