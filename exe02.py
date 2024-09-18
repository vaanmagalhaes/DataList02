# Lista Encadeada:
# 2. Remova duplicatas de uma lista ordenada. Suponha que lhe seja fornecida uma
# lista encadeada armazenando números inteiros em ordem crescente. Sua tarefa é
# remover todos os elementos duplicados da lista. Por exemplo, dada a lista
# [0 → 1 → 1 → 5 → 7 → 10 → 10 → None], seu programa deve retornar a lista
# [0 → 1 → 5 → 7 → 10 → None].

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

    def remove_duplicates(self):
        current = self.head
        while current:
            next_distint = current.next
            while next_distint and next_distint.data == current.data:
                next_distint = next_distint.next
                current.next = next_distint
                current = next_distint
        return LinkedList


l = LinkedList()
l.insert_at_beginning(10)
l.insert_at_beginning(9)
l.insert_at_beginning(8)
l.insert_at_beginning(8)
l.insert_at_beginning(7)
l.insert_at_beginning(6)
l.insert_at_beginning(6)
l.insert_at_beginning(5)
l.insert_at_beginning(4)
l.insert_at_beginning(3)
l.insert_at_beginning(3)
l.insert_at_beginning(2)
l.insert_at_beginning(1)
l.insert_at_beginning(0)
print(l)