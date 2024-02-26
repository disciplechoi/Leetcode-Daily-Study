"""
* Review
- 1st : 2/24/2024
- 2nd :


* Solution
1) 

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 4-3-2-1 링크드 리스트 생성
def create_linked_list():
    # 노드 1 생성 (값: 1)
    node1 = ListNode(1)

    # 노드 2 생성 (값: 2, 다음 노드는 노드 1)
    node2 = ListNode(2, node1)

    # 노드 3 생성 (값: 3, 다음 노드는 노드 2)
    node3 = ListNode(3, node2)

    # 노드 4 생성 (값: 4, 다음 노드는 노드 3)
    node4 = ListNode(4, node3)

    # 생성한 노드를 헤드로 하는 링크드 리스트 반환
    return node4


linked_list_head = create_linked_list()


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:

    first_node = head
    current = head

    while current.next:

        temp = current

        if current.val > current.next.val:

            temp.next = current
            current.next = current.next.next

        current = current.next


sortList(linked_list_head)
