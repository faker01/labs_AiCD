def prefix(s):
    v = [0]*len(s)
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v


with open("input.txt", "r") as f:
    data = f.read()

sample = input()


index = 0
f = prefix(sample)
c = 0
while index != -1:

    index = -1
    k = 0
    for i in range(len(data)):
        while k > 0 and sample[k] != data[i]:
            k = f[k-1]
        if sample[k] == data[i]:
            k = k + 1
        if k == len(sample):
            index = i - len(sample) + 1
            break
    if index != -1:
        data = data[index + len(sample)::]
        print(index + c)
        c += index + len(sample)