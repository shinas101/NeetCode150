class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if not digits:
            return [1]

        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        else:
            return self.plusOne(digits[:-1]) + [0]
        
