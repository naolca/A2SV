class Solution:
    def kClosest(self, points, k):
        list_2b_returned = []
        tempo   = []
        
        for x in points:
            actual = x
            d = ((actual[0]-0)**2)+((actual[1]-0)**2)
            tempo.append([d, actual])
        
        tempo.sort()
        
        for x in range(k):
            temp = tempo[x]
            list_2b_returned.append(temp[1])
            
        return list_2b_returned
        