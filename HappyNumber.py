class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = self.sqr(n)
            if n == 1:
                return True
        return False

    def sqr(self, n:int) -> int:
        output = 0

        while n:
            temp = n % 10
            temp = temp ** 2
            output += temp
            n = n //10
        return output



        
