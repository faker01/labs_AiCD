def check(str):
    brackets = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
    f = False
    for k in range(len(str)):
        if str[k] in "{}[]()":
            brackets[str[k]] += 1
            if brackets['('] < brackets[')'] or brackets['['] < brackets[']'] or brackets['{'] < brackets['}']:
                f = True
                break
    if f or brackets['('] != brackets[')'] or brackets['['] != brackets[']'] or brackets['{'] != brackets['}']:
        return False
    else:
        return True

"""
s = input("Введите строку\n")

if check:
    print("Строка существует")
else:
    print("Строка не существует")"""