class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Добавляет элемент в конец очереди"""
        self.items.append(item)

    def dequeue(self):
        """Удаляет и возвращает элемент из начала очереди"""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def front(self):
        """Возвращает элемент из начала очереди без удаления"""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("front from empty queue")

    def is_empty(self):
        """Проверяет, пуста ли очередь"""
        return len(self.items) == 0

    def size(self):
        """Возвращает размер очереди"""
        return len(self.items)

# Пример использования
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Вывод: 1
print(queue.front())    # Вывод: 2
print(queue.is_empty()) # Вывод: False