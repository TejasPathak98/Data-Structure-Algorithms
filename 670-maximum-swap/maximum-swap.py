class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(digit) for digit in str(num)]
        m_stack = []

        for i in range(len(nums)):
            while m_stack and nums[m_stack[-1]] < nums[i]:
                m_stack.pop()
            m_stack.append(i)
        
        for i in range(len(nums)):
            if nums[i] != nums[m_stack[i]]:
                break
            
        j = i + 1
        while j < len(m_stack) and nums[m_stack[i]] == nums[m_stack[j]]:
            j += 1
        
        j -= 1

        print(m_stack)
        #print(j,nums[m_stack[j]])

        nums[i] , nums[m_stack[j]] = nums[m_stack[j]] , nums[i]

        print(nums)

        return int(''.join(map(str,nums)))
        