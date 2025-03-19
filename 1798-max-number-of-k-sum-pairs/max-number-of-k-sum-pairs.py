class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        counter = Counter(nums)

        for num in nums:
            if counter[num] > 0:
                if k - num in counter and counter[k - num] > 0:
                    if num == k - num:
                        if counter[num] >= 2:
                            count += 1
                            counter[num] -= 2
                        else:
                            continue
                    else:
                        counter[num] -= 1
                        counter[k - num] -= 1
                        count += 1

        return count

