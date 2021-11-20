def roundf(base):
    count = -1
    while 2 ** count > base:
        count -= 1

    return -count

def float_bin(base):
    res = '0.'
    for _ in range(15):
        base *= 2
        res += str(int(base // 1))
        base %= 1

    return res

def replace_all(text, words):
    res = ''
    while len(text) != 0:
        end = True
        for i in words:
            if i == text[:len(i)]:
                end = False
                res += words[i]
                text = text[len(i):]

        if end:
            break

    return res

def separator(text):
    res = []
    while len(text) != 0:
        res.append(int(text[:8] + '0' * (8 - len(text[:8])), 2))
        text = text[8:]

    return res

delimiter = '😶'
