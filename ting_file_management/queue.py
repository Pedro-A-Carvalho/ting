from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self._data = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self._data)

    def is_empty(self):
        return self._data == []

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self._data.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        if not self.is_empty():
            return self._data.pop(0)  # O(n)
        else:
            return None

    def search(self, index):
        """Aqui irá sua implementação"""
        if index < 0 or index >= len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
