from func import delimiter, replace_all

def decod(filename):
    with open(filename, 'rb') as f:
        text = f.read()
        text = text.split(delimiter.encode('utf-8'))
        byte = []
        voc = {}

        for i in text[:len(text) - 1:]:
            byte.append(i.decode('utf-8'))

        for i in range(2, int(byte[0]) * 2 + 1, 2):
            voc[byte[i + 1]] = chr(int(byte[i]) - int(byte[1]))

        text = list(text[-1])
        bin_text = ''
        for i in text:
            bin_text += bin(int(i))[2:].zfill(8)

    filename = (filename.split('.'))[0]

    with open(f'{filename}.txt', 'w') as f:
        f.write(replace_all(bin_text, voc))