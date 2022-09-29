class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list_2b_returned = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dumy = 0
                if nums1[i] == nums2[j]:
                    
                    for k in range(j+1, len(nums2)):
                        if nums2[k] > nums2[j]:
                            list_2b_returned.append(nums2[k])
                            dumy = 1
                            break
                    if dumy != 1:
                        list_2b_returned.append(-1)
        return list_2b_returned
        