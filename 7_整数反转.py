class Solution:
    def reverse(self, x: int) -> int:
        # if x <= -2**31 or x >= 2**31-1:
        #     return 0
        # return  int(str(x)[::-1]) if x>=0 else -int(str(abs(x))[::-1])

        if x<0:
            return -self.reverse(abs(x))
        reverse_x = int(str(x)[::-1])
        if -2**31< reverse_x < 2**31-1:
            return reverse_x
        else:
            return 0


        