from Element import Element


class MinHeap():
    def __init__(self):
        self.lst: list[Element] = []

    def min(self):
        if self.lst:
            return self.lst[0]
        return None

    def extract_min(self):
        if not self.lst:
            return None
        self._swap(0, len(self.lst) - 1)
        res = self.lst.pop()

        # maintain Min Heap property
        self._shift_down(0)

        return res

    def insert(self, ele: Element):
        self.lst.append(ele)

        # maintain Min Heap property
        self._shift_up(len(self.lst) - 1)

    def search(self, value) -> int:
        for index, item in enumerate(self.lst):
            if item.val == value:
                return index, item
        return -1, None

    def update(self, i: int, ele: Element):
        old = self.lst[i]

        self.lst[i] = ele

        if ele < old:
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

    def _shift_down(self, i: int):
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

    def _shift_up(self, i: int):
        if i == 0:
            return
        p = self._parent(i)
        if self.lst[i] < self.lst[p]:
            self._swap(i, p)
            self._shift_up(p)

