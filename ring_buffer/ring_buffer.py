# class RingBuffer:
#     def __init__(self, capacity, data=[]):
#         self.index = 0
#         self.capacity = capacity
#         self.data = list(data)[capacity:]

#     def append(self, item):
#         if len(self.data) == self.capacity:
#             self.data[self.index] = item
#         else:
#             self.data.append(item)
#         self.index = (self.index + 1) % self.capacity

#     def get(self):
#         return(self.data)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        # Check if storage is empty
        if len(self.storage) == 0:
            # If it is we append item
            self.storage.append(item)
        else:
            # Check if storage is at capacity
            if len(self.storage) == self.capacity:
                # Check if index is at capacity
                if self.index == self.capacity:
                    # If it is we then zero out the index
                    self.index -= self.capacity
                    # Then we add the item into storage at the index
                    self.storage[self.index] = item
                    # Then we increment the index by 1
                    self.index += 1
                # If the index is not at capacity
                else:
                    # We add the item into storage at the index
                    self.storage[self.index] = item
                    # Then we increment the index
                    self.index += 1
                # If storage is not at capacity
            else:
                # We then just add item to storage
                self.storage.append(item)

    def get(self):
        # Retur the list
        return self.storage
