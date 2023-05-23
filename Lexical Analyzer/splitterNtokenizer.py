def wordSplitter(filename):
    file = open(filename, 'r')
    content = file.read()
    words = []
    curnt_word = ""
    for char in content:
        if (char == ' ' or char == '\t' or char == '\n'):
            if len(curnt_word) > 0:
                words.append(curnt_word)
                curnt_word = ""
        elif char == '+':
            if len(curnt_word) > 0 and curnt_word[-1] == "=":
                if len(curnt_word) > 2:
                    words.append(curnt_word[:-2])
                curnt_word = "+="
                continue
            curnt_word += char
    if len(curnt_word) > 0:
        words.append(curnt_word)

    for word in words:
        print(word)


wordSplitter('f.txt')
