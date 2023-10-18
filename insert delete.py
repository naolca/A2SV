class RandomizedSet:

    def __init__(self):
        self.num_idx = {}

        self.nums = []
     
    def insert(self, val: int) -> bool:
        if val in self.num_idx:
            return False
        
       
        self.num_idx[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_idx or not self.num_idx:
            return False
        
        idx = self.num_idx[val]

        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]

        self.num_idx[self.nums[idx]] = idx
        
        del self.num_idx[val]

        self.nums.pop()
        
        return True

    def getRandom(self) -> int:
        random_idx = random.randint(0, len(self.nums) - 1)
        return self.nums[random_idx]
