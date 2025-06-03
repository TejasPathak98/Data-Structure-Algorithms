class NumberContainers:

    def __init__(self):
        self.number_dict = defaultdict(list)
        self.index_dict = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_dict:
            self.index_dict[index] = number
            heappush(self.number_dict[number], index)
        else:
            self.index_dict[index] = number
            heappush(self.number_dict[number], index)

    def find(self, number: int) -> int:
        if number not in self.number_dict:
            return -1
        else:
            # while self.number_dict[number]:
            #     idx = heappop(self.number_dict[number])
            #     if self.index_dict[idx] == number:
            #         heappush(self.number_dict[number], item)
            #         return idx
            # return -1

            while self.number_dict[number] and self.index_dict[self.number_dict[number][0]] != number:
                heappop(self.number_dict[number])

            if self.number_dict[number]:
                return self.number_dict[number][0]
            else:
                return -1


        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)