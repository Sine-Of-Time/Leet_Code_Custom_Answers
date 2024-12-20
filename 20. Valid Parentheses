class Solution:
    def isValid(self, s: str) -> bool:
       #The main idea behind this is that due to the config of char, an closing bracket will always be right after the corresponding open one in a valid string
       stack = []
       hMap = {")": "(", "]": "[" ,"}": "{"} #Mapping each close to open

       for c in s:
        if c in hMap:
            if stack and stack[-1] == hMap[c]: #This is ensuring the stack is not empty via stack and checking if the newest element, which
                stack.pop()                    # is always stack[-1] in python, is matching to an closing version.
            else:
                return False
        else:
            stack.append(c) #else add opening bracket, which is the only ones we need to add
       return True if not stack else False
