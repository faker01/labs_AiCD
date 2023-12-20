from random import choice
import os
import heapq



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
    max_digits = max([len(str(x)) for x in lst])
    base = 10
    bins = [[] for _ in range(base)]
    for i in range(max_digits):
        for x in lst:
            digit = (x // base ** i) % base
            bins[digit].append(x)
        lst = [x for queue in bins for x in queue]
        bins = [[] for _ in range(base)]
    return lst


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
    if len(lst) < 2:
        return lst[:]
    else:
        mid = int(len(lst) / 2)
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        q = choice(lst)
    l_nums = [n for n in lst if n < q]

    e_nums = [q] * lst.count(q)
    b_nums = [n for n in lst if n > q]
    return quick_sort(l_nums) + e_nums + quick_sort(b_nums)


def external_sort(lst, chunk_size):
    chunk = []
    chunk_count = 0

    for i in range(len(lst)):
        chunk.append(lst[i])
        if len(chunk) == chunk_size:
            chunk.sort()

            with open(f'chunk_{chunk_count}.tmp', 'w') as chunk_file:
                for num in chunk:
                    chunk_file.write(f"{num}\n")

            chunk_count += 1
            chunk = []

    # Merge the sorted chunks using heapq
    files = [open(f'chunk_{i}.tmp', 'r') for i in range(chunk_count)]
    merged = list(heapq.merge(*files, key=lambda x: int(x)))
    for i in range(len(merged)):
        merged[i] = merged[i][:len(merged[i])-1]
    for i in files:
        i.close()
    # Clean up temporary files
    for i in range(chunk_count):
        os.remove(f'chunk_{i}.tmp')
    return merged







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
list_ = [1, 0, 7, -5, 6, 4]
print(quick_sort(list_))
list_ = [1, 0, 7, -5, 6, 4]
print(external_sort(list_, 2))
list_ = [1, 0, 7, 5, 6, 4]
print(tree_sort(list_))