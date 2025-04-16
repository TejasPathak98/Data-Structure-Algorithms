class FileSystem:

    def __init__(self):
        self.file_dict = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.file_dict:
            return False
        
        slash_count = 0
        for ch in path:
            if ch == '/':
                slash_count += 1
        if slash_count == 1:
            self.file_dict[path] = value
            return True
        else:
            parent = path.split('/')[:-1]
            if '/'.join(parent) not in self.file_dict:
                return False
            else:
                self.file_dict[path] = value
                return True

    def get(self, path: str) -> int:
        if path not in self.file_dict:
            return -1
        else:
            return self.file_dict[path]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)