class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        def check(radius):
            for val in houses:
                ind=bisect_left(heaters,val)
                if val-heaters[ind-1]>radius and heaters[ind]-val>radius:
                    return False
                
            return True
        heaters.sort()
        houses.sort()
        heaters = [float('-inf')] + heaters + [inf]
        l, r = 0, 2e10 + 1
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return int(l)
            
        
