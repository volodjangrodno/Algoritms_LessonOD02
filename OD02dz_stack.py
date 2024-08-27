class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавляет элемент на вершину стека"""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Возвращает элемент с вершины стека без удаления"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """Проверяет, пуст ли стек"""
        return len(self.items) == 0

    def size(self):
        """Возвращает размер стека"""
        return len(self.items)

# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Вывод: 3
print(stack.peek())  # Вывод: 2
print(stack.is_empty())  # Вывод: False