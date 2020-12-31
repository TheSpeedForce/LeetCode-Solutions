class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sList =[]
        tList = []
        sList[:0] = s
        tList[:0] = t
        sList.sort()
        tList.sort()
        if sList == tList:
            return True
        else:
            return False
        
