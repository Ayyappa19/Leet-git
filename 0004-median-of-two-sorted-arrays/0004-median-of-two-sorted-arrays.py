class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1+nums2
        k=sorted(l)
        le=len(k)
        if(le%2==0):
            i=(le//2)-1
            j=i+1
            return(k[i]+k[j])/2
            
        
        else:
            return(k[le//2])

        