class Solution:
    def maximumSwap(self, num: int) -> int:
        my_num = [int(digit) for digit in str(num)]

        def solve(my_num):
            if not my_num:
                return my_num
            max_number = max(my_num)
            if my_num[0] == max_number:
                return [max_number] + solve(my_num[1:])
            else:
                pos = my_num[::-1].index(max_number)
                pos = pos + 1
                my_num[-pos] , my_num[0] = my_num[0] , my_num[-pos]
                return my_num        
        
        return int(''.join(str(digit) for digit in solve(my_num)))
