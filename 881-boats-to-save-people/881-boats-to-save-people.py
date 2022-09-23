class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        current = 0
        people.sort()
        final = len(people)-1
        
        while current <= final:
            if people[current] + people[final] <= limit:
                current += 1
                final -= 1
            else:
                final -= 1
            boats += 1
        return boats