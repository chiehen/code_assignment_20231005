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


class MinHeap():
    def __init__(self):
        self.lst = []

    def extract_min(self):
        if len(self.lst) == 0:
            return
        self._swap(0, len(self.lst) - 1)
        res = self.lst.pop()

        # maintain Min Heap property
        self._shift_down(0)

        return res

    def insert(self, val, priority, order):
        ele = Element(val, priority, order)
        self.lst.append(ele)

        # maintain Min Heap property
        self._shift_up(len(self.lst) - 1)

    def search(self, value) -> int:
        for index, item in enumerate(self.lst):
            if item.val == value:
                return index
        return -1

    def change_priority(self, i: int, new_prio: int):
        old_prio = self.lst[i].priority
        self.lst[i].priority = new_prio
        if new_prio < old_prio:
            self._shift_up(i)
        else:
            self._shift_down(i)

    def _swap(self, i: int, j: int):
        self.lst[i], self.lst[j] = self.lst[j], self.lst[i]

    def _parent(self, i: int):
        return (i - 1) // 2

    def _l_child(self, i: int):
        if 2 * i + 1 < len(self.lst):
            return 2 * i + 1
        return None

    def _r_child(self, i: int):
        if 2 * i + 2 < len(self.lst):   
            return 2 * i + 2
        return None

    def _shift_down(self, i):
        l_child = self._l_child(i)
        r_child = self._r_child(i)
        min_index = i
        if l_child and self.lst[min_index] > self.lst[l_child]:
            min_index = l_child
        if r_child and self.lst[min_index] > self.lst[r_child]:
            min_index = r_child

        if i != min_index:
            self._swap(i, min_index)
            self._shift_down(min_index)

    def _shift_up(self, i):
        if i == 0:
            return
        p = self._parent(i)
        if self.lst[i] < self.lst[p]:
            self._swap(i, p)
            self._shift_up(p)

    def print_prio(self):
        for ele in self.lst:
            print(ele.priority)


