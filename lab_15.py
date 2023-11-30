from lab_1 import check


def straight(inp):  # done
    if "," not in inp:
        return inp

    lst = inp.split(" ")

    if inp[len(lst[0]) - 1] != ",":
        cur = inp.index("(")
        end = inp.index(")")
        while not check(inp[cur + 1:end]):
            end += inp[end + 1:].index(")") + 1
        return lst[0] + " " + straight(inp[len(lst[0]) + 2:end]) + " " + straight(inp[end + 3:])
    else:
        lst1 = inp.split(", ")
        return lst1[0] + " " + straight(inp[len(lst1[0]) + 2:])


def central(inp): # done
    if "," not in inp:
        return inp

    lst = inp.split(" ")
    if inp[len(lst[0]) + 1] == "(":
        cur = inp.index("(")
        end = inp.index(")")
        p = inp.index(",")
        while not check(inp[cur + 1:end]):
            end += inp[end + 1:].index(")") + 1
        while not check(inp[cur + 1:p + 1]):
            p += inp[p + 1:end].index(",") + 1
        return central(inp[cur + 1:p]) + " " + lst[0] + " " + central(inp[p + 2:end])
    elif inp[len(lst[0])] == ",":
        return lst[0] + " " + central(inp[len(lst[0])+1:])


def reversive(inp):  # done
    if "," not in inp:
        return inp

    lst = inp.split(" ")

    if inp[len(lst[0]) - 1] != ",":
        cur = inp.index("(")
        end = inp.index(")")
        while not check(inp[cur + 1:end]):
            end += inp[end + 1:].index(")") + 1
        return reversive(inp[len(lst[0]) + 2:end]) + " " + lst[0] + " " + reversive(inp[end + 3:])
    else:
        lst1 = inp.split(", ")
        return lst1[0] + " " + reversive(inp[len(lst1[0]) + 2:])


inputt = "8 (3 (1, 6 (4, 7)), 10 (, 14 (13, )))"
strr = straight(inputt)
strr = strr.replace("  ", " ")
print(strr)

inputt = "8 (3 (1, 6 (4, 7)), 10 (, 14 (13, )))"
strr = central(inputt)
strr = strr.replace("  ", " ")
print(strr)

inputt = "8 (3 (1, 6 (4, 7)), 10 (, 14 (13, )))"
strr = reversive(inputt)
strr = strr.replace("  ", " ")
print(strr)