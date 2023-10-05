def bubble_sort(lst, flag):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if (lst[j] > lst[j + 1]) == flag:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def insertion_sort(lst, flag):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and ((lst[j] < lst[j - 1]) == flag):
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
    return lst


def selection_sort(lst, flag):
    for i in range(len(lst)):
        if flag:
            mn = lst.index(min(lst[i::]))
            lst[i], lst[mn] = lst[mn], lst[i]
        else:
            mx = lst.index(max(lst[i::]))
            lst[i], lst[mx] = lst[mx], lst[i]
    return lst


def shell_sort(lst, flag):
    last_index = len(lst)
    step = len(lst) // 2
    while step > 0:
        for i in range(step, last_index):
            j = i
            delta = j - step
            while delta >= 0 and (lst[delta] > lst[j]) == flag:
                lst[delta], lst[j] = lst[j], lst[delta]
                j = delta
                delta = j - step
        step //= 2
    return lst





list_ = [1, 0, 7, -5, 6, 4]
print(bubble_sort(list_, True))
list_ = [1, 0, 7, -5, 6, 4]
print(insertion_sort(list_, True))
list_ = [1, 0, 7, -5, 6, 4]
print(selection_sort(list_, True))
list_ = [1, 0, 7, -5, 6, 4]
print(shell_sort(list_, True))
list_ = [1, 0, 7, -5, 6, 4]
print(shell_sort(list_, True))