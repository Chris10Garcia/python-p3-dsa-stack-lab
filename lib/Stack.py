class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def push(self, item):
        if len(self.items) != self.limit:
            self.items.append(item)
        # else:
        #     raise Exception

    def pop(self):
        return self.items.pop() if len(self.items) > 0 else None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return True if self.limit == len(self.items) else False

    def search(self, target):
        items_to_search = self.items.copy()
        counter = 0

        while len(items_to_search) > 0:
            if items_to_search.pop() == target:
                return counter
            elif len(items_to_search) == 0:
                return -1
            else:
                counter += 1
        # for x in range(len(items_to_search)):
        #     item = items_to_search.pop()
        #     print(item, counter, target)

        #     if item == target:
        #         print("this should return")
        #         return counter
        #     else:
        #         counter += 1

        # return "What is going on"




      
stk = Stack([5,6,7,8,9,10])

print(stk.search(5))
print(stk.search(6))
print(stk.search(7))
print(stk.search(8))
print(stk.search(9))
