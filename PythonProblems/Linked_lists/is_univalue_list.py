class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def is_univalue_list(head):
  current = head
  while current is not None and current.next is not None:
    if current.val == current.next.val:
      current = current.next
    else:
      return False
  return True

###Solution 2###
def is_univalue_list(head):
  current = head
  while current is not None:
    if current.val != head.val:
      return False
    current = current.next
  return True
