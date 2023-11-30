class Stack:
    def __init__(self):
        self.lst = []

    def push(self, elem):
        self.lst.append(elem)

    def pop(self):
        if len(self.lst) > 0:
            elem = self.lst[len(self.lst) - 1]
            self.lst = self.lst[:len(self.lst) - 1]
            return elem
        else:
            return None


def splt(strr):
    s = 0
    l = []

    for i in range(len(strr)):
        if strr[i] in "(), ":
            l.append(strr[s:i])
            s = i + 1

    while "" in l:
        l.remove("")

    return l


stk = Stack()
inputt = "8 (3 (1, 6 (4, 7)), 10 (, 14 (13, )))"
lst = splt(inputt)

for i in range(1, len(lst) + 1):
    stk.push(lst[-i])

for i in range(len(lst)):
    print(stk.pop(), end=" ")