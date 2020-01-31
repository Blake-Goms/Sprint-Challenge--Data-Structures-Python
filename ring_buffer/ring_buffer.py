from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity > self.storage.__len__():
            self.storage.add_to_head(item)
        else:
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        temp = 0
        while temp < self.storage.__len__():
            selectedHead = self.storage.head
            list_buffer_contents.append(selectedHead.value)
            self.storage.move_to_front(selectedHead)
            temp += 1
        return list_buffer_contents



# test = RingBuffer(4)
# test.append('a')
# test.append('b')
# test.append('c')
# test.append('d')
# test.append('e')
# print(test.get())



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
