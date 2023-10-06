from MinHeap import MinHeap
from Element import Element


class PriorityQueue():
    def __init__(self):
        self.heap: MinHeap = MinHeap()
        self.order: int = 0

    def dequeue(self):
        ele = self.heap.extract_min()

        if ele is not None:
            return ele.val
        return None

    def insert(self, val, priority: int):
        ele = Element(val, priority, self.order)
        self.heap.insert(ele)
        self.order += 1

    def peek(self):
        ele = self.heap.min()

        if ele is not None:
            return ele.val
        return None

    def change_priority(self, val, new_priority: int):
        index, ele = self.heap.search(val)

        if index == -1:
            print("Value isn't in the queue")
            return

        new_ele = Element(ele.val, new_priority, ele.order)
        self.heap.update(index, new_ele)
