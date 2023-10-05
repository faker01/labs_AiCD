from lab_1 import check


s = input()
nums = [""]
signs = []
if check(s):
    j = 0
    for i in range(len(s)):
        if s[i] in '0123456789':
            nums[j] += s[i]
        elif nums[j] != "":
            nums[j] = int(nums[j])
            j += 1
            nums.append("")
    if nums[-1] == "":
        nums.remove("")

    for i in range(len(s)):
        if s[i] not in '0123456789=':
            signs.append(s[i])
    cur = 0
    end = len(signs)
    while len(signs) > 0:
        if cur > len(signs) - 1:
            cur = 0
        elif cur == end:
            end = len(signs) - 1
            cur = 0
        elif '(' in signs[cur:end]:
            cur = signs.index("(")
            end = signs.index(")") - 1
            signs.pop(cur)
            signs.pop(end)
        elif "*" in signs[cur:end] and "/" in signs[cur:end]:
            if signs.index("*", cur, end) < signs.index("/", cur, end):
                res = nums[signs.index("*", cur, end)] * nums[signs.index("*", cur, end) + 1]
                nums[signs.index("*", cur, end)] = res
                nums.pop(signs.index("*", cur, end) + 1)
                signs.pop(signs.index("*", cur, end))
            else:
                res = nums[signs.index("/", cur, end)] / nums[signs.index("/", cur, end) + 1]
                nums[signs.index("/", cur, end)] = res
                nums.pop(signs.index("/", cur, end) + 1)
                signs.pop(signs.index("/", cur, end))
            end -= 1
        elif "*" in signs[cur:end]:
            res = nums[signs.index("*", cur, end)] * nums[signs.index("*", cur, end) + 1]
            nums[signs.index("*", cur, end)] = res
            nums.pop(signs.index("*", cur, end) + 1)
            signs.pop(signs.index("*", cur, end))
            end -= 1
        elif "/" in signs[cur:end]:
            res = nums[signs.index("/", cur, end)] / nums[signs.index("/", cur, end) + 1]
            nums[signs.index("/", cur, end)] = res
            nums.pop(signs.index("/", cur, end) + 1)
            signs.pop(signs.index("/", cur, end))
            end -= 1
        elif "+" in signs[cur:end] and "-" in signs[cur:end]:
            if signs.index("+", cur, end) < signs.index("-", cur, end):
                res = nums[signs.index("+", cur, end)] + nums[signs.index("+", cur, end) + 1]
                nums[signs.index("+", cur, end)] = res
                nums.pop(signs.index("+", cur, end) + 1)
                signs.pop(signs.index("+", cur, end))
            else:
                res = nums[signs.index("-", cur, end)] - nums[signs.index("-", cur, end) + 1]
                nums[signs.index("-", cur, end)] = res
                nums.pop(signs.index("-", cur, end) + 1)
                signs.pop(signs.index("-", cur, end))
            end -= 1
        elif "+" in signs[cur:end]:
            res = nums[signs.index("+", cur, end)] + nums[signs.index("+", cur, end) + 1]
            nums[signs.index("+", cur, end)] = res
            nums.pop(signs.index("+", cur, end) + 1)
            signs.pop(signs.index("+", cur, end))
            end -= 1
        elif "-" in signs[cur:end]:
            res = nums[signs.index("-", cur, end)] - nums[signs.index("-", cur, end) + 1]
            nums[signs.index("-", cur, end)] = res
            nums.pop(signs.index("-", cur, end) + 1)
            signs.pop(signs.index("-", cur, end))
            end -= 1
    print(nums[0])