# Lista Encadeada
# 1. Implemente a função remove utilizando a função busca.

class NodoList:
    def __init__(self, data=0, next_nodo=None):
        self.data = data
        self.next = next_nodo

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "[" + str(self.head) + "]"

    def insert_at_beginning(self, new_data):
        new_nodo = NodoList(new_data)
        new_nodo.next = self.head
        self.head = new_nodo

    def remove(self):
        value = int(input('Enter a number of the list do delete'))
        previous = None
        current = self.head
        while current and current.data != value:
            previous = current
            current = current.next
        if current:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
            print(f'{value} was removed of the list.')
        else:
            print(f'{value} not found in the list.')



l = LinkedList()
l.insert_at_beginning(10)
l.insert_at_beginning(18)
l.insert_at_beginning(420)
l.insert_at_beginning(92)
l.insert_at_beginning(78)
l.insert_at_beginning(2)
l.insert_at_beginning(65)
l.insert_at_beginning(84)
print(l)

l.remove()
print(f'List after removal: {l}')