class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
         #first i will start by creating a list to store the elements in nums as numbers
        list_used=[]
        #next i will appent elements of nums to list_use by casting them to integers
        for string_number in nums:
            list_used.append(int(string_number))
        list_used = sorted(list_used)
        #next i will reverse the list so that the firs element is the 1st lsrgest element in the list
        list_used.reverse()
        #finally i will return the needed number as a string
        return str(list_used[k-1])
        