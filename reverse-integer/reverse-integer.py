class Solution:
    def reverse(self, x: int) -> int:
        if x:
            var= (x//abs(x))*(int(str(abs(x))[::-1]))
            if (-2**31)<=var<=(2**31)-1:
                return var
        return 0
        
