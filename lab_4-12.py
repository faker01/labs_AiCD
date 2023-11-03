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


def tree_sort(lst):
    return True

def heapify(lst, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and lst[left_child] > lst[largest]:
        largest = left_child

    if right_child < heap_size and lst[right_child] > lst[largest]:
        largest = right_child

    if largest != root_index:
        lst[root_index], lst[largest] = lst[largest], lst[root_index]
        heapify(lst, heap_size, largest)


def heap_sort(lst):
    for i in range(len(lst), -1, -1):
        heapify(lst, len(lst), i)

    for i in range(len(lst) - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k] = lefthalf[i]
                i = i + 1
            else:
                lst[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            lst[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            lst[k] = righthalf[j]
            j = j + 1
            k = k + 1


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
list_ = [1, 0, 7, -5, 6, 4]
print(heap_sort(list_))
list_ = [1, 0, 7, -5, 6, 4]
print(merge_sort(list_))
