class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end="->" if current.next else "")
        current = current.next
    print()

arr = [1, 2, 3, 4, 5]
linked_list_head = array_to_linked_list(arr)
print("LinkedList:", end=" ")
print_linked_list(linked_list_head)
