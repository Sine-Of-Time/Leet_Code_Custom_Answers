class Solution:
    def isValid(self, s: str) -> bool:
      #Hashmap
      Map = {")":"(","}":"{","]":"["}
      st=[]
      for char in s:
        if(char in Map):#We need to ensure that we only process chars otherwise we ill have an error
            if(st and st[-1]==Map[char]):
                st.pop()
            else: #If it is an closing with no opening, we return false
                return False
        else:
            st.append(char)
      return not len(st)     
