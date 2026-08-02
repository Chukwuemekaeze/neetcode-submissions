class Solution:
    def hasDuplicate(self, nums:list) -> bool:
        empty = set()
        for n in nums:
            if n in empty:
                return True
            empty.add(n)
        return False