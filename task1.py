class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        cur = self.head
        last = None

        while cur:
            next = cur.next
            cur.next = last
            last = cur
            cur = next

        self.head = last

    def sort(self):
        current = self.head

        while current:
            min_node = current
            search = current.next

            # Знайдемо мінімальний вузол в несортованій частині
            while search:
                if search.data < min_node.data:
                    min_node = search
                search = search.next

            # Обмінюємо значення поточного вузла з мінімальним знайденим вузлом
            current.data, min_node.data = min_node.data, current.data

            # Переходимо до наступного вузла в списку
            current = current.next

    def merge(self, other):
        element_to_merge = other.head

        while element_to_merge:
            next = element_to_merge.next
            target = self.head

            while target:
                inner_next = target.next

                if element_to_merge.data > target.data:
                    target = inner_next
                    continue

                other.delete_node(element_to_merge.data)

                # Якщо елементи рівні, просто вставляємо елемент наступним
                if element_to_merge.data == target.data:
                    element_to_merge.next = target.next
                    target.next = element_to_merge
                    break

                if element_to_merge.data < target.data:
                    element_to_merge.next = target.next
                    target.next = element_to_merge
                    element_to_merge.data, target.data = target.data, element_to_merge.data
                    break

                target = inner_next

            element_to_merge = next


        if other.head:
            tail = self.head

            while tail.next:
                tail = tail.next

            tail.next = other.head

        return self


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

llist.print_list()

llist.reverse()

print()

llist.print_list()

print()

llist.sort()
llist.print_list()



llist2 = LinkedList()

# Вставляємо вузли в початок
llist2.insert_at_beginning(21)
llist2.insert_at_beginning(31)
llist2.insert_at_beginning(11)
llist2.sort()

print()

llist.merge(llist2)
llist.print_list()