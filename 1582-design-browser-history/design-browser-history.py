class BrowserHistory:

    def __init__(self, homepage: str):
        self.queue = []
        self.queue.append(homepage)
        self.website_ptr = 0
        
    def visit(self, url: str) -> None:
        self.queue = self.queue[:self.website_ptr + 1]
        self.queue.append(url)
        self.website_ptr += 1

    def back(self, steps: int) -> str:
        if self.website_ptr - steps <= 0:
            self.website_ptr = 0
            return self.queue[0]
        else:
            x = self.website_ptr - steps
            self.website_ptr -= steps
            return self.queue[x]

    def forward(self, steps: int) -> str:
        if self.website_ptr + steps >= len(self.queue) - 1:
            self.website_ptr = len(self.queue) - 1
            return self.queue[-1]
        else:
            x = self.website_ptr + steps
            self.website_ptr += steps
            return self.queue[x]



        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)