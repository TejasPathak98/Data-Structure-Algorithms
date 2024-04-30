class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n = n - 1 
        binary_n = list(bin(n)[2:])
        binary_x = list(bin(x)[2:])
        curr_n = len(binary_n) - 1 

        for i in range(len(binary_x) - 1, -1 , -1):
            if binary_x[i] == "1":
                continue 
            binary_x[i] = binary_n[curr_n]
            curr_n = curr_n - 1 

            if curr_n == -1:
                break  
            
        if curr_n >= 0:
            binary_x =  binary_n[0:curr_n + 1] + binary_x
        
        return int("".join(binary_x),2)




        