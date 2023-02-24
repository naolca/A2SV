class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        main=Counter(s1)
        candidate=defaultdict(int)
        left=0
        ans=False
        for right in range(len(s2)):
            candidate[s2[right]]+=1
            if right-left+1==len(s1):
                if main==candidate:
                    ans=True
                    break
                candidate[s2[left]]-=1
                if candidate[s2[left]]==0:
                    del candidate[s2[left]]
                left+=1
        return ans

