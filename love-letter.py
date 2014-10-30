import string
T = int(raw_input(''))
c = dict(zip(string.ascii_lowercase, range(1,27))) 
for i in range(T):
    text = raw_input()
    end = len(text) - 1
    num = int(len(text)/2)
    count = 0
    for i in range(num):
        diff = c[text[i]] - c[text[end-i]]
        if diff > 0:
            count = count + diff
        elif diff < 0:
            count = count - diff

    print count
