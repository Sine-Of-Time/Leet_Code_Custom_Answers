import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strL = s.lower()
        s = re.sub(r'[^a-z0-9]','',strL)
        l=0
        h=len(s)-1
        while(h>l):
            if(s[h]!=s[l]):
                return False
            l=l+1
            h=h-1
        return True 
