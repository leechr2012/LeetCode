# Write a function, linked_list_values, that takes in the head of a linked list as an argument.
# The function should return a list containing all values of the nodes in the linked list.

#iterative time O(n) and space O(n)
def linked_list_values(head):
  values = []
  current = head
  while current is not None:
    values.append(current.val)
    current = current.next
  return values

#recursive time O(n) and space O(n)
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
  new_list = []
  while head is not None:
    new_list.append(head.val)
    head = head.next
  return new_list
