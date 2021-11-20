from func import roundf, float_bin, replace_all, separator, delimiter

def encod(filename, offset):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        repeat = {w : text.count(w) for w in set(text)}
        remains = {w : repeat[w] / len(text) for w in repeat}

        for i in remains:

            repeat[i] = roundf(remains[i])

        a = {}
        count = 0
        for i in sorted(repeat, key=lambda x: repeat[x]):

            a[i] = float_bin(count)[2:repeat[i] + 2]
            count += remains[i]

        b = replace_all(text, a)
        bute = separator(b)

    filename = (filename.split('.'))[0]

    with open(f'{filename}.prar', 'wb') as fa:
        toencode = [len(repeat), int(offset)]
        for i in a:
            toencode.append(ord(i) + int(offset))
            toencode.append(a[i])
        for i in toencode:
            fa.write(str(i).encode('utf-8'))
            fa.write(delimiter.encode('utf-8'))
        fa.write(bytes(bute))