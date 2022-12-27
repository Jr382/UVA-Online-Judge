from sys import stdin as s


class Block:

    def __init__(self, value):
        self.previous = None
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)

    def __iter__(self):
        current = self
        while current:
            yield current
            current = current.next

    def stack(self, other):
        if not self.in_same_stack(other):
            if other.previous is not None:
                other.previous.next = None
            last = self.get_last()
            last.next, other.previous = other, last

    def in_same_stack(self, other):
        return self.get_first() == other.get_first()

    def unstack(self):
        blocks = [] if self.next is None else list(self.next)
        for block in blocks:
            block.next, block.previous = None, None
        self.next = None

    def get_last(self):
        current = self
        while current.next:
            current = current.next
        return current

    def get_first(self):
        current = self
        while current.previous:
            current = current.previous
        return current

    def _move_onto(self, other):
        self.unstack()
        other.unstack()
        other.stack(self)

    def _move_over(self, other):
        self.unstack()
        other.stack(self)

    def _pile_onto(self, other):
        other.unstack()
        other.stack(self)

    def _pile_over(self, other):
        other.stack(self)

    def operate(self, operation, mode, other):
        if not self.in_same_stack(other):
            if operation == "move":
                if mode == "onto":
                    self._move_onto(other)
                else:
                    self._move_over(other)
            else:
                if mode == "onto":
                    self._pile_onto(other)
                else:
                    self._pile_over(other)


def main():
    line = s.readline().strip()
    blocks = [Block(i) for i in range(int(line))]
    line = s.readline().strip()
    while line != "quit":
        operation, value, mode, target = line.split()
        value, target = int(value), int(target)
        blocks[value].operate(operation, mode, blocks[target])
        line = s.readline().strip()
    format_blocks(blocks)


def format_blocks(blocks):
    for i in range(len(blocks)):
        pile = f'{i}:'
        if blocks[i].previous is None:
            pile += " " + " ".join([str(block) for block in blocks[i]])
        print(pile)


main()

