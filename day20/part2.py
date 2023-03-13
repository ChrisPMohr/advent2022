from collections import defaultdict, Counter


class DoubleLinkedNode(object):

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.is_head = False

    def move(self, length):
        moves = self.data % (length - 1)
        for _ in range(moves):
            was_head = self.is_head
            if self.next.is_head:
                self.next.is_head = False
                self.is_head = True
            elm0 = self.prev
            elm1 = self
            elm2 = self.next
            elm3 = self.next.next
            elm0.next = elm2
            elm1.prev = elm2
            elm1.next = elm3
            elm2.prev = elm0
            elm2.next = elm1
            elm3.prev = elm1
            if was_head:
                self.is_head = False
                elm2.is_head = True
        # else:
        #     moves = (-1 * self.data) % length
        #     print(moves)
        #     for _ in range(moves):
        #         was_head = self.is_head
        #         if self.prev.is_head:
        #             self.prev.is_head = False
        #             self.is_head = True
        #         elm0 = self.prev.prev
        #         elm1 = self.prev
        #         elm2 = self
        #         elm3 = self.next
        #         elm0.next = elm2
        #         elm1.prev = elm2
        #         elm1.next = elm3
        #         elm2.prev = elm0
        #         elm2.next = elm1
        #         elm3.prev = elm1
        #         if was_head:
        #             self.is_head = False
        #             elm3.is_head = True


class DoubleLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add_to_front(self, data):
        node = DoubleLinkedNode(data)
        if self.head is None:
            self.head = node
            self.tail = node
            node.is_head = True
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.len += 1

    def link_ends(self):
        self.tail.next = self.head
        self.head.prev = self.tail

    def mix(self):
        ordered_nodes = []
        ptr = self.head
        while ptr:
            ordered_nodes.append(ptr)
            if ptr == self.head.prev:
                break
            ptr = ptr.next
        self.print()
        for _ in range(10):
            for node in ordered_nodes:
                node.move(self.len)
                if node.is_head:
                    self.head = node
                # self.print()
            # self.print()

    def print(self):
        ptr = self.head
        while not ptr.is_head:
            ptr = ptr.next
        head = ptr
        while ptr:
            print(ptr.data, end=", ")
            if ptr == head.prev:
                break
            ptr = ptr.next
        print()

    def get_important_values(self):
        ptr = self.head
        while not ptr.data == 0:
            ptr = ptr.next

        ret = []
        for _ in range(1000):
            ptr = ptr.next
        ret.append(ptr.data)
        for _ in range(1000):
            ptr = ptr.next
        ret.append(ptr.data)
        for _ in range(1000):
            ptr = ptr.next
        ret.append(ptr.data)
        return ret


def main():
    # lines = open('example.txt', 'r').readlines()
    lines = open('input.txt', 'r').readlines()
    # line = open('example.txt', 'r').readline()
    # line = open('input.txt', 'r').readline()
    # nums = list(map(int, open('example.txt', 'r').readline().split(',')))  # Nums on one line
    # nums = list(map(int, open('input.txt', 'r').readline().split(',')))  # Nums on one line

    l = DoubleLinkedList()

    key = 811589153

    for line in lines:
        d = int(line.strip())
        l.add_to_front(d * 811589153)

    l.link_ends()
    l.mix()
    print(sum(l.get_important_values()))



    # items = {}
    # for y, line in enumerate(lines):
    #     for x, c in enumerate(line.strip()):
    #         items[(x, y)] = int(c)

    # max_x = max(x for x,y in items)
    # max_y = max(y for x,y in items)
    # for y in range(0, max_y + 1):
    #     print("".join('#' if (x,y) in items else ' ' for x in range(0, max_x+10)))


if __name__ == '__main__':
    main()
