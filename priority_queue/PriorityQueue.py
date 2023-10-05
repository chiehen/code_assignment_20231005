from MinHeap import MinHeap


class Element():
    def __init__(self, val, priority, order):
        self.priority = priority
        self.val = val
        self.order = order

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        elif self.priority == other.priority and self.order < other.order:
            return True

        return False

    def __gt__(self, other):
        if self.priority > other.priority:
            return True
        elif self.priority == other.priority and self.order > other.order:
            return True

        return False


class PriorityQueue():
    def __init__(self):
        self.heap = MinHeap()
        self.order = 0

    def dequeue(self):
        ele = self.heap.extract_min()

        if ele is not None:
            return ele.val
        return None

    def insert(self, val, priority):
        ele = Element(val, priority, self.order)
        self.heap.insert(ele)
        self.order += 1

    def peek(self):
        return self.heap.min()

    def change_priority(self, val, new_priority):
        index, ele = self.heap.search(val)

        if index == -1:
            print("Value doesn't in the queue")
            return

        new_ele = Element(ele.val, new_priority, ele.order)
        self.heap.update(index, new_ele)
