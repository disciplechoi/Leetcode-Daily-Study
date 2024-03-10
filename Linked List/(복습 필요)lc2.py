# 1. 두개의 리스트의 길이가 다른데 언제가지 for 문을 돌려야 하는 건지 모르겠다.
# 2. 덧셈을 했을 떄 10 이상의 숫자가 나올 수 있는데 두개의 digit을 배열 한자리에 따로 넣어야 하는것이 중요하다.
# 3. 배열 크기를 미리 선언할 수 없다.
# 4. 배열을 마지막에 리버스 해야한다. => 거꾸로 된 것이 좋음. 어차피 덧셈은 뒤에서 시작함.


# linked list concept


# node = head
# while node :
#     print(node.val)
#     print(node.next)
#     node = node.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(2)
current = l1

current.next = ListNode(4)
current = current.next

current.next = ListNode(3)
current = current.next

l2 = ListNode(5)
current = l2

current.next = ListNode(6)
current = current.next

current.next = ListNode(4)
current = current.next


total = ListNode(0)
current = total
carry = 0


while l1 or l2 or carry != 0:
    result = l1.val + l2.val + carry
    carry = 0

    if result >= 10:
        carry = result // 10
        current.next = ListNode(result % 10)

    else:
        current.next = ListNode(result)
    current = current.next

    if l1.next:
        l1 = l1.next
    if l2.next:
        l2 = l2.next
# while l1!=None or l2!=None  or carry !=0:
#     val1 = l1.val if l1 else 0
#     val2= l2.val if l2 else 0
#     sum = val1+val2+carry

#     if sum>=10 :
#         carry = sum//10
#     else :
#         carry = 0

#     current.next= ListNode(sum%10)
#     current = current.next

#     l1=l1.next if l1 else None
#     l2=l2.next if l2 else None


while total:
    print(total.val)
    total = total.next
