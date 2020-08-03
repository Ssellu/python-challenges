"""
    자료구조의 종류 중 '단일연결리스트'라는 구조가 있습니다.
    단일연결리스트는 노드(데이터)를 논리적으로 연결한 단방향 구조를 일컫습니다.
    논리적 연결은 현재 노드가 이웃 노드의 주소를 참조함으로써 구현합니다.

        가장 앞 노드는 head에 기록합니다.
        마지막 노드는 next 를 None 으로 기록합니다.



    head : 0x100

        0x100 번지        0x200 번지        0x300 번지        0x400 번지
        data | next      data | next      data | next      data | next
        10    0x200      20     0x300     30    0x400      40     None



"""


class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class SinglyLinkedList:
    head: Node = None

    def add(self, data: int):
        pass

    def order(self):
        tmp = SinglyLinkedList.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

lst = SinglyLinkedList()
lst.add(10)
lst.add(100)
lst.add(20)
lst.add(30)
lst.add(1250)

# 10 100 20 30 1250 순으로 데이터가 출력될 수 있도록 add()를 완성하세요.
