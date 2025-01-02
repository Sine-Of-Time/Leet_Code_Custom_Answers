# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      #The idea behind the following code is that we will use two pointers to transverse to the end of the code and the middle, then reverse the middle pointer and compair each value to ensure they are the same  
      #This is the improved solution with o(1) memory use
      fast = head
      slow = head

      #This section of the code get our slow pointer to the middle and our fast pointer to the end
      while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

      #This section reverses the middle pointer direction by creating an seperate reversed linked list  
      prev = None
      while slow:
        tmp = slow.next #Using tmp to preserve the .next pointer
        slow.next = prev #Setting this specific slow nodes .next to point to prev making it the first element in the new list 
        prev = slow #Setting the new "head" of reversed linked listing pointer prev to its proper location
        slow = tmp #Setting the new current "slow" node to the next one in the main "Proper order" linked list
      
      #Check palindrome
      left,right = head,prev
      while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
      return True
