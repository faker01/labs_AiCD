from lab_1 import check


def take_str(node, str_tree):
    if "(" in str_tree:
        cur = str_tree.index("(")
        end = str_tree.index(")")

        while not check(str_tree[cur + 1:end]):
            end += str_tree[end + 1:].index(")") + 1

        if "," in str_tree:
            p = str_tree.index(",")

            while not check(str_tree[cur + 1:p + 1]):
                p += str_tree[p + 1:end].index(",") + 1

    elif "," in str_tree:
        cur = 0
        end = len(str_tree)
        p = str_tree.index(",")

        while not check(str_tree[cur + 1:p + 1]):
            p += str_tree[p + 1:end].index(",") + 1

    elif str_tree == "":
        return Tree_node(node)

    else:
        cur = 0
        p = -1

    el1 = el2 = ''

    k1 = cur + 1
    while str_tree[k1] not in "(), ":
        el1 += str_tree[k1]
        k1 += 1

    if p != -1:
        s2 = k2 = p + 2
        while str_tree[k2] not in "(), ":
            el2 += str_tree[k2]
            k2 += 1
    else:
        el2 = ""

    tr = Tree_node(node)
    tr.add_2_sides(take_str(el1, str_tree[k1:s2 - 2]), take_str(el2, str_tree[k2 + 1:end]))
    return tr


class Tree_node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def left_node(self):
        return self.left

    def right_node(self):
        return self.right

    def take_value(self):
        return self.value

    def add(self, val, side):
        if side == "+":
            self.left = val
        elif side == "-":
            self.right = val

    def add_2_sides(self, val1, val2):
        self.left = val1
        self.right = val2

    def delete(self, side):
        if side == "+":
            self.left = None
        elif side == "-":
            self.right = None


inpp = "(3 (1, 6 (4, 7)), 10 (, 14 (13, )))"

t = take_str("8", inpp)

while True:
    input_ = input("Что Вы хотите сделать:\n1 - добавить элемент в пустую ячейку\n2 - удалить элемент\n3 - изменить элемент\n")
    if input_ == "0":
        break
    elif input_ == "1":  # добавить
        tr = [t]
        if tr[-1] != None:
            inp = input('Добавление в данную ячейку недоступно. Введите сторону("+" - лево, "-" - право\n')
            while inp != "":
                if tr[-1] == None:
                    print("Ячейка найдена")
                    break

                if inp == "+":
                    tr.append(tr[-1].left_node())

                    if tr[-1] == None:
                        print("Ячейка найдена")
                        break

                    if tr[-1].left_node() == None:
                        print("Доступна ячейка слева")
                    if tr[-1].right_node() == None:
                        print("Доступна ячейка справа")

                elif inp == "-":
                    tr.append(tr[-1].right_node())

                    if tr[-1] == None:
                        print("Ячейка найдена")
                        break

                    if tr[-1].left_node() == None:
                        print("Доступна ячейка слева")
                    if tr[-1].right_node() == None:
                        print("Доступна ячейка справа")
                inp = input('Добавление в данную ячейку недоступно. Введите сторону("+" - лево, "-" - право\n')

        inp1 = input("Введите элемент, который хотите добавить: ")
        tr[-1] = Tree_node(inp1)
        if len(tr) > 1:
            if inp == "+":
                tr[-2].left = tr[-1]
            else:
                tr[-2].right = tr[-1]
        print("добавлен элемент {}".format(inp1))
        while len(tr) > 1:
            if tr[-1] == tr[-2].left_node():
                tr[-2].left = tr[-1]
            elif tr[-1] == tr[-2].right_node():
                tr[-2].right = tr[-1]
            tr = tr[:len(tr) - 1]
        t = tr[0]


    elif input_ == "2" and t != None:  # удалить
        f = True
        tr = [t]
        inp = input('Введите сторону("+" - лево, "-" - право, "enter" - остановиться)\n')
        while inp != "":
            if inp == "+":
                tr.append(tr[-1].left_node())
            elif inp == "-":
                tr.append(tr[-1].right_node())
            if tr[-1] == None:
                print("вы упустили момент, тут нельзя удалить элемент(. Попробуйте ещё раз")
                f = False
                break
            inp = input()

        print("значение {} удалено".format(tr[-1].value))
        tr[-1] = None

        while len(tr) > 1:
            if tr[-1] == tr[-2].left_node():
                tr[-2].left = tr[-1]
            elif tr[-1] == tr[-2].right_node():
                tr[-2].right = tr[-1]
            tr = tr[:len(tr) - 1]
        t = tr[0]

    elif input_ == "3" and t != None:  # вставить
        f = True
        tr = [t]
        inp = input('Введите сторону("+" - лево, "-" - право, "enter" - остановиться)\n')
        while inp != "":
            if inp == "+":
                tr.append(tr[-1].left_node())
            elif inp == "-":
                tr.append(tr[-1].right_node())
            else:
                print("неправильный ввод")
                f = False
                break

            if tr[-1] == None:
                print("вы упустили момент, тут нельзя изменить элемент(. Попробуйте ещё раз")
                f = False
                break
            inp = input()

        if f:
            inp = input('Введите значение: ')
            print("значение {} изменено на {}".format(tr[-1].value, inp))
            tr[-1].value = inp

            while len(tr) > 1:
                if tr[-1] == tr[-2].left_node():
                    tr[-2].left = tr[-1]
                elif tr[-1] == tr[-2].right_node():
                    tr[-2].right = tr[-1]
                tr = tr[:len(tr) - 1]
            t = tr[0]

    else:
        print("неправильный ввод")
