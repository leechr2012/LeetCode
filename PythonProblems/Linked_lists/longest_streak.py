# Write a function, longest_streak, that takes in the head of a linked list as an argument.
# The function should return the length of the longest consecutive streak of the same value within the list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def longest_streak(head):
    if head is None:
        return 0

    current = head
    current_streak = 1
    max_streak = 0

    while current.next is not None:
        if current.val == current.next.val:
            current_streak += 1
        else:
            if current_streak > max_streak:
                max_streak = current_streak
            current_streak = 1
        current = current.next

    if current_streak > max_streak:
      max_streak = current_streak

    return max_streak
