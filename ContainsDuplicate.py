# LC 217
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        st = set()
        for num in nums:
            if num in st:
                return True
            else:
                st.add(num)
        return False
        
