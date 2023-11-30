class Hash_func:
    def __init__(self, inp):
        self.lst = {}
        l = 0
        for i in range(len(inp)):
            if inp[i] not in self.lst.values():
                self.lst[l] = inp[i]
                l += 1

    def hash_table(self):
        return self.lst



with open("input.txt", "r") as f:
    hash_ = Hash_func(f.read())

table = hash_.hash_table()
with open("output.txt", "w") as f:
    for i in table.keys():
        f.write("{}: {}, ".format(i, table[i]))