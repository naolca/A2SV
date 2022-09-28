class MyCircularDeque:

    def __init__(self, k: int):
        self.items = []
        self.k = k
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size == self.k:
            return False
        self.items.insert(0, value)
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.k:
            return False
        self.items.append(value)
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size > 0:
            self.items.pop(0)
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.size > 0:
            self.items.pop()
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        if self.size > 0:
            return self.items[0]
        return False

    def getRear(self) -> int:
        if self.size == 0:
            return -1
        if self.size > 0:
            return self.items[-1]
        return False

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()