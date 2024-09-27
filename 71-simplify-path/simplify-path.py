class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)

        pa = path.split("/")
        pa = [x for x in pa if x != '' and x != '.']
        idx = set()
        i = 0

        my_stack = []

        for x in pa:
            if x != '..':
                my_stack.append(x)
            else:
                if my_stack:
                    my_stack.pop()
        

        print(pa)

        # while i < len(pa):
        #     if pa[i] == '..':
        #         idx.add(i - 1)
        #     i += 1
        
        # print(idx)
        # offset = 0

        # for index in idx:
        #     if index - offset >= 0:
        #         pa.pop(index - offset)
        #         offset += 1
            
        # pa = [x for x in pa if x != '..']
        
        print(my_stack)

        return '/' + '/'.join(my_stack)

        #for i in range(n):


        