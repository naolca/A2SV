class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        points=[0]*n
        maxPoint=[0]*n
        points[-1]=questions[-1][0]
        maxPoint[-1]=points[-1]
        for i in range(n-1,-1,-1):
            points[i]=questions[i][0]
            nextindex=i+questions[i][1]+1
            if nextindex<n:
                points[i]+=maxPoint[nextindex]
            if i!=n-1:
                maxPoint[i]=max(maxPoint[i+1],points[i])
        return maxPoint[0]