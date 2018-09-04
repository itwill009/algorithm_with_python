class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first = Node("dummy")


class linked:

    def __init__(self,data):

        self.data = Node(data)


li = linked(123)


print(li.data.data)
print(li.data.next)
