from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()


    def append(self, item):
        if self.current == None:
            self.current = 0 

        current_head = self.storage.head
        # if our head is None, move item to tail
        if current_head is None:
            self.storage.add_to_tail(item)
            self.current += 1
            return
        else:
            # loop through current
            for i in range(self.current):
                # if next node/element is not None
                if current_head.next != None:
                    # then set that next node/element to current_head
                    current_head = current_head.next
                else:
                    # if next node/element is None
                    # put item at tail
                    self.storage.add_to_tail(item)
                    self.current += 1
                    if self.current == self.capacity:
                        self.current = 0
                    return
            current_head.value = item
            self.current += 1
            if self.current == self.capacity:
                self.current = 0

    def get(self):
        #Note:  This is the only [] allowed
        list_buffer_contents = []
        temp = 0
        while temp < self.storage.__len__(): # loop through storage
            current_head = self.storage.head # grab head
            list_buffer_contents.append(current_head.value) # append head value to list
            self.storage.move_to_end(current_head) # move head to tail
            temp += 1
        return list_buffer_contents



#     def append(self, item):
#         if self.capacity > self.storage.__len__():
#             self.storage.add_to_head(item)
#         else:
#             self.storage.remove_from_tail()
#             self.storage.add_to_head(item)




# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
