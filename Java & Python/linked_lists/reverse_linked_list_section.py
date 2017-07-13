# find start pos, find prev, start reversing
# temp = prev, temp.next = prev, move to next nodes
class Solution:
    # func: reverse a linked list from position m to n
    # @param head: head node of the list
    # @param m: starting position m
    # @param n: ending position n
    # @return: new head node
    def reverseBetween(self, head, m, n):
        root = ListNode(0)
        root.next = head
        #Find position m
        prev = root
        count = 1
        while count < m:
            prev = prev.next
            count += 1
        start = prev
        end = start.next
     
        #Start reversing
        prev = prev.next
        temp = prev.next
        while count < n:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
            count += 1
     
        start.next = prev
        end.next = curr
     
        return root.next