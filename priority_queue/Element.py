class Element():
    def __init__(self, val, priority, order):
        self.priority: int = priority
        self.val = val
        self.order: int = order

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