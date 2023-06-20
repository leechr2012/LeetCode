# Write a function, insert_node, that takes in the head of a linked list, a value, and an index.
# The function should insert a new node with the value into the list at the specified index.
# Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

# Do this in-place.

# You may assume that the input list is non-empty and the index is not greater than the length of the input list.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  node_index = 0
  current = head
  if index == 0:
    current = Node(value)
    current.next = head
    return current

  while current is not None:
    if node_index == index - 1:
      temp = current.next
      current.next = Node(value)
      current.next.next = temp

    current = current.next
    node_index += 1
  return head
