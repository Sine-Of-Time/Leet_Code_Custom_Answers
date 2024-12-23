class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        #Did not even have to look for help with this one, quite proud of progress
        cntrL,cntrR,cntr_=0,0,0
        for i in range(len(moves)):
            if moves[i] == 'L':
                cntrL += 1
            if moves[i] == 'R':
                cntrR += 1
            if moves[i] == '_':
                cntr_ += 1 
        majV,minV=0,0           
        if cntrL > cntrR:
            print("In cntrL")
            majV=cntrL
            minV=cntrR
        elif cntrR > cntrL:
            print("In cntrR")
            majV=cntrR
            minV=cntrL
        else:
            print("In else")
            majV=minV=L
        return (cntr_+majV)-minV        
