# Write a function, get_node_value, that takes in the head of a linked list and an index.
# The function should return the value of the linked list at the specified index.

# If there is no node at the given index, then return None.

#Solution with O(n) time complexity.
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index):
  counter = 0
  while head is not None:
    if counter == index:
      return head.val
    else:
      head = head.next
      counter += 1
  return None
