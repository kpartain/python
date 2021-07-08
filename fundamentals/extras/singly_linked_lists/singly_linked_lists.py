class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def add_to_back(self, val):
        new_node = SLNode(val)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
        return self
    def remove_from_front(self):
            #in progress, optional
        return self

    def remove_from_back(self):
            #in progress, optional
        return self

    def remove_val(self, val):
        head_val = self.head
        if head_val is not None:
            if head_val.value == val:
                self.head = head_val.next
                head_val = None
            return
        while head_val is not None:
            if head_val.data == val:
                break
            prev = head_val
            head_val = head_val.next
        if head_val is None:
            return
        prev.next = head_val.next
        head_val = None
        return self

    def insert_at(self, val, n):
            #in progress, optional
        return self

    def print_values(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next
        return self
my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()