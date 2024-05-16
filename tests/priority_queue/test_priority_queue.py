from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    p_queue = PriorityQueue()
    p_queue.enqueue({"qtd_linhas": 7})
    p_queue.enqueue({"qtd_linhas": 3})
    p_queue.enqueue({"qtd_linhas": 5})
    p_queue.enqueue({"qtd_linhas": 1})
    assert len(p_queue) == 4
    assert p_queue.dequeue() == {"qtd_linhas": 3}
    assert p_queue.search(2) == {"qtd_linhas": 5}
    with pytest.raises(IndexError):
        p_queue.search(len(p_queue) + 1)
    with pytest.raises(IndexError):
        p_queue.search(-1)
