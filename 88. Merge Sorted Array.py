class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       l = (n+m) - 1
       while n and m: #need to decrement n and m each time so they do not cuz the loop to terminate early 
         if nums1[m-1] > nums2[n-1]:
            nums1[l]=nums1[m-1]
            m-=1
         else:
            nums1[l] = nums2[n-1]
            n -= 1
         l -= 1 #Decrement shared variables seperatly 
    
       while n: #Append any elements left in nums2 to the front of nums1
            nums1[l] = nums2[n-1]    
            l -= 1
            n -= 1
