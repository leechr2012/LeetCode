# Write a function, add_lists, that takes in the head of two linked lists, each representing a number.
# The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head.
# The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

# You must do this by traversing through the linked lists once.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_lists(head_1, head_2):
    current_1 = head_1
    current_2 = head_2
    carry = 0
    result_head = None
    result_tail = None

    while current_1 or current_2 or carry:
        val1 = current_1.val if current_1 else 0
        val2 = current_2.val if current_2 else 0

        # Calculate the sum and carry
        total_sum = val1 + val2 + carry
        digit = total_sum % 10
        carry = total_sum // 10

        # Create a new node with the digit
        node = Node(digit)

        if result_head is None:
            result_head = node
            result_tail = node
        else:
            result_tail.next = node
            result_tail = node

        # Move to the next nodes
        current_1 = current_1.next if current_1 else None
        current_2 = current_2.next if current_2 else None

    return result_head
