from lab_17 import Tree_node, take_str


def to_lst(strr):
    el = ""
    list_ = []
    for k in range(len(strr)):
        if strr[k] in "0123456789":
            el += strr[k]
        elif el != "":
            list_.append(el)
            el = ""
    return list_


def change_values(strr, list_):
    for k in range(len(strr)):
        if strr[k] in "0123456789":
            strr = strr[:k] + ":" + strr[k + 1:]
    while "::" in strr:
        strr = strr.replace("::", ":")
    for k in range(len(list_)):
        strr = strr.replace(":", list_[k], 1)
    return strr


inpp = "8 (3 (1, 6 (4, 7)), 10 (, 14 (13, )))"

lst = to_lst(inpp)
lst.sort(key=lambda x: int(x))

inp = change_values(inpp, lst)
print(inp)

