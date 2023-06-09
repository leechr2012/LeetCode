class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  # initializing dummy_head to tail allows you to have a separate reference (tail)
  # that you can manipulate to build the merged list while keeping the head of the merged list intact in dummy_head.
  current_1 = head_1
  current_2 = head_2

  while current_1 is not None and current_2 is not None:
    if current_1.val < current_2.val:
      tail.next = current_1
      current_1 = current_1.next
    else:
      tail.next = current_2
      current_2 = current_2.next
    tail = tail.next 

#After the intitial while loop, if the lists arent of equal length, one will return None which will break the while loop
# if there are remaining numbers in either list, this will append the remainder of this list to the merged list.
  if current_1 is not None:
    tail.next = current_1

  if current_2 is not None:
    tail.next = current_2

  return dummy_head.next
