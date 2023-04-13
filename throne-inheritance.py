class ThroneInheritance:

    def __init__(self, kingName: str):
        # self.d=defaultdict(list)
        self.king=kingName
        self.adjecencyList=[]
        self.dead=set()

        
        

    def birth(self, parentName: str, childName: str) -> None:
        self.adjecencyList.append([parentName,childName])


        
        

    def death(self, name: str) -> None:
        self.dead.add(name)


        

    def getInheritanceOrder(self) -> List[str]:
        # print(self.dead)
        d=defaultdict(list)
        for p,c in self.adjecencyList:
            d[p].append(c)
        # print(d)
        res=[]
        def dfs(node):
            nonlocal res
            if node not in self.dead:
                res.append(node)
            for child in d[node]:
                dfs(child)
               
        dfs(self.king)
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()