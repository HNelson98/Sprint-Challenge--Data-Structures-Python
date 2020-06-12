# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.data = []
#         self.storage = [None]*capacity

#     class __Full:
#         def append(self, item):
#             if self.cur > self.capacity:
#                 self.cur = 0
#             else:
#                 self.cur =+ 1
#             self.data[self.cur] = item

#         def get(self):
#             return self.data

#     def append(self, item):
#         # Check the Capacity
#         # if not at cap jsut insert
#         # if at cap then replace the oldest
#         if len(self.data) == self.capacity:
#             self.cur = 0
#             self.__class__ = self.__Full
            
#         else:
#             self.data.append(item)

#     def get(self):
#         return(self.data)

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.cur = 0

    def append(self, item):
        # Check the Capacity
        # if not at cap jsut insert
        # if at cap then replace the oldest
        if len(self.data) == self.capacity:
            if self.cur == self.capacity -1:
                self.data[self.cur] = item
                self.cur = 0
            else:
                self.data[self.cur] = item
                self.cur += 1
                

        else:
            self.data.append(item)

    def get(self):
        return(self.data)

buffer = RingBuffer(5)
for i in range(50):
    buffer.append(i)
print(buffer.cur)
print(buffer.get())
