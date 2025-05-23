class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        x = n
        temp = []

        while x:
            temp.append(x % 10)

            x = x // 10

        temp = temp[::-1]

        l = len(temp)
        i = l - 2

        while i >= 0:
            if temp[i] >= temp[i + 1]:
                i -= 1
            else:
                break

        if i == -1:
            return -1
        
        pos = i

        for j in range(l - 1,pos,-1):
            if temp[pos] >= temp[j]:
                continue
            else:
                break
        
        temp[pos] , temp[j] = temp[j] , temp[pos]

        temp[pos + 1:] = sorted(temp[pos + 1:])

        st = ""

        for y in temp:
            st = st + chr(ord('0') + y)
        
        if int(st) > 2**31 - 1 or int(st) < -2 ** 31:
            return -1
        else:
            return int(st)



        



        

