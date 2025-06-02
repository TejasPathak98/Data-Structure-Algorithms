class StockSpanner:

    def __init__(self):
        
        self.stack = []

    def next(self, price: int) -> int:

        curr_stack = self.stack

        curr_price , curr_span = price , 1

        while curr_stack and price >= curr_stack[-1][0]:
            
            stack_price , stack_span = curr_stack.pop()

            curr_span += stack_span
        
        curr_stack.append((curr_price,curr_span))

        return curr_span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)