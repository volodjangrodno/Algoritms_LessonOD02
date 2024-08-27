class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


queue = Queue()

print(queue.is_empty())

queue.enqueue('Действие 1')
queue.enqueue('Действие 2')
queue.enqueue('Действие 3')
queue.enqueue('Действие 4')

# ['Действие 4', 'Действие 3', 'Действие 2', 'Действие 1'] - вот так сейчас выглядит наш список
print(queue.is_empty())
print(queue.size())

print(queue.dequeue())

print(queue.size())