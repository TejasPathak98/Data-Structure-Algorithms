class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for sh in shift:
            direction = sh[0]
            amount = sh[1] % len(s)

            if direction == 0:
                partition = s[:amount]
                new_s = s[amount:] + partition
                s = new_s
            else:
                partition = s[-amount:]
                new_s = partition + s[:-amount]
                s = new_s
        
        return s
        