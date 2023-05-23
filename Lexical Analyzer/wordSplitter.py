from functions import FunctionsClass


def wordSplitter(lineString, position):

    arr = [None] * (2)
    i = position
    ch = ''
    word = ""
    while (i < len(lineString)):
        ch = lineString[i]

        if (ch == ' ' or ch == '\t' or ch == '\n'):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                break
            else:
                i += 1
                continue

        elif (ch == '!'):
            if (i + 1 < len(lineString) and lineString[i + 1] == '='):
                if (word != ""):
                    arr[0] = word
                    arr[1] = str(i)
                    word = ""
                    break
                else:
                    word = "!="
                    arr[0] = word
                    arr[1] = str(i + 2)
                    word = ""
                    break
            else:
                word = word + str(ch)
        elif (ch == ':'):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            if (i + 1 < len(lineString) and lineString[i + 1] == '='):
                word = ":="
                arr[0] = word
                arr[1] = str(i + 2)
                word = ""
                break
            else:
                word = word + str(ch)
                arr[0] = word
                arr[1] = str(i + 1)
                word = ""
                break
        elif (ch == '>'):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            if (i + 1 < len(lineString) and lineString[i + 1] == '='):
                word = ">="
                arr[0] = word
                arr[1] = str(i + 2)
                word = ""
                break
            else:
                word = word + str(ch)
                arr[0] = word
                arr[1] = str(i + 1)
                word = ""
                break
        elif (ch == '<'):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            if (i + 1 < len(lineString) and lineString[i + 1] == '='):
                word = "<="
                arr[0] = word
                arr[1] = str(i + 2)
                word = ""
                break

            else:
                word = word + str(ch)
                arr[0] = word
                arr[1] = str(i + 1)
                word = ""
                break
        elif (ch == '='):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            if (i + 1 < len(lineString) and lineString[i + 1] == '='):
                word = "=="
                arr[0] = word
                arr[1] = str(i + 2)
                word = ""
                break
            else:
                word = word + str(ch)
                arr[0] = word
                arr[1] = str(i + 1)
                word = ""
                break
        elif (ch == '|'):
            if (i + 1 < len(lineString) and lineString[i + 1] == '|'):
                if (word != ""):
                    arr[0] = word
                    arr[1] = str(i)
                    word = ""
                    break
                else:
                    word = "||"
                    arr[0] = word
                    arr[1] = str(i + 2)
                    word = ""
                    break
            else:
                word = word + str(ch)
        elif (ch == '+'):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            if (i + 1 < len(lineString) and lineString[i + 1] == ':'):
                if (i + 2 < len(lineString) and lineString[i + 2] == "="):
                    word = "+:="
                    arr[0] = word
                    arr[1] = str(i + 3)
                    word = ""
                    break
            elif (i + 1 < len(lineString) and lineString[i + 1] == '+'):
                word = "++"
                arr[0] = word
                arr[1] = str(i + 2)
                word = ""
                break
            else:
                word = word + str(ch)
                arr[0] = word
                arr[1] = str(i + 1)
                word = ""
                break

        elif (ch == '-'):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            if (i + 1 < len(lineString) and lineString[i + 1] == ':'):
                if (i + 2 < len(lineString) and lineString[i + 2] == "="):
                    word = "-:="
                    arr[0] = word
                    arr[1] = str(i + 3)
                    word = ""
                    break
            elif (i + 1 < len(lineString) and lineString[i + 1] == '>'):
                word = "->"
                arr[0] = word
                arr[1] = str(i + 2)
                word = ""
                break
            elif (i + 1 < len(lineString) and lineString[i + 1] == '-'):
                word = "--"
                arr[0] = word
                arr[1] = str(i + 2)
                word = ""
                break
            else:
                word = word + str(ch)
                arr[0] = word
                arr[1] = str(i + 1)
                word = ""
                break

        elif (ch == '/'):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            if (i + 1 < len(lineString) and lineString[i + 1] == ':'):
                if (i + 2 < len(lineString) and lineString[i + 2] == "="):
                    word = "/:="
                    arr[0] = word
                    arr[1] = str(i + 3)
                    word = ""
                    break
            else:
                word = word + str(ch)
                arr[0] = word
                arr[1] = str(i + 1)
                word = ""
                break

        elif (ch == '*'):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            if (i + 1 < len(lineString) and lineString[i + 1] == ':'):
                if (i + 2 < len(lineString) and lineString[i + 2] == "="):
                    word = "*:="
                    arr[0] = word
                    arr[1] = str(i + 3)
                    word = ""
                    break
            else:
                word = word + str(ch)
                arr[0] = word
                arr[1] = str(i + 1)
                word = ""
                break

        elif (ch == '%' or ch == '(' or ch == ')' or ch == '{' or ch == '}' or ch == '[' or
              ch == ']' or ch == ';' or ch == ','):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            else:
                word = word + ch
                arr[0] = word
                arr[1] = str(i + 1)
                word = ""
                break

        elif (ch == '\''):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            word = word + str(ch)
            i += 1
            if (i < len(lineString)):
                ch = lineString[i]
                word = word + str(ch)
                if (ch == '\\'):
                    j = 0
                    while (j < 2):
                        i += 1
                        if (i < len(lineString)):
                            ch = lineString[i]
                            word = word + str(ch)
                        j += 1
                    arr[0] = word
                    arr[1] = str(i + 1)
                    word = ""
                    break
                else:
                    i += 1
                    if (i < len(lineString)):
                        ch = lineString[i]
                        word = word + str(ch)
                        arr[0] = word
                        arr[1] = str(i + 1)
                        word = ""
                        break
        elif (ch == '"'):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            while True:
                ch = lineString[i]
                if (ch == '\\' and i + 1 < len(lineString)):
                    word = word + str(ch) + lineString[i + 1]
                    i += 1
                else:
                    word = word + str(ch)
                i += 1
                if ((i < len(lineString) and lineString[i] != '"') == False):
                    break

            if (i < len(lineString) and lineString[i] == '"'):
                word = word + "\""
                arr[0] = word
                arr[1] = str(i + 1)
                word = ""
                break
        elif (ch == "'"):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            while True:
                ch = lineString[i]
                if (ch == '\\' and i + 1 < len(lineString)):
                    word = word + str(ch) + lineString[i + 1]
                    i += 1
                else:
                    word = word + str(ch)
                i += 1
                if ((i < len(lineString) and lineString[i] != "'") == False):
                    break

            if (i < len(lineString) and lineString[i] == "'"):
                word = word + "\'"
                arr[0] = word
                arr[1] = str(i + 1)
                word = ""
                break
        elif (ch == '`'):
            if (word != ""):
                arr[0] = word
                arr[1] = str(i)
                word = ""
                break
            i = len(lineString)
        elif (ch == '.'):
            if (word != ""):
                if (FunctionsClass.int_check(word)):
                    i += 1
                    if (i < len(lineString)):
                        ch = lineString[i]
                        if (FunctionsClass.int_check(ch)):
                            word = word + "." + ch
                        else:
                            arr[0] = word
                            arr[1] = str(i)
                            word = ""
                            break
                    else:
                        i -= 1
                        arr[0] = word
                        arr[1] = str(i)
                        word = ""
                        break
                else:
                    arr[0] = word
                    arr[1] = str(i)
                    word = ""
                    break
            else:
                word = word + "."
                i += 1
                if (i < len(lineString)):
                    ch = lineString[i]
                    if (FunctionsClass.int_check(ch)):
                        word = word + str(ch)
                    else:
                        arr[0] = word
                        arr[1] = str(i)
                        word = ""
                        break
                else:
                    arr[0] = word
                    arr[1] = str(i)
                    word = ""
                    break
        else:
            word = word + str(ch)
        i += 1
    if (word != ""):
        arr[0] = word
        arr[1] = str(i)
        word = ""
    elif (arr[0] == None and arr[1] == None):
        arr[0] = "-1"
        arr[1] = str(i + 1)
    return arr


result = []
file = open('f.txt', 'r')
lines = file.readlines()

for line in lines:
    if (line):
        if line[0] != "#":

            index = 0

            while (index < len(line)):
                arr = wordSplitter(line, index)
                index = int(arr[1])
                word = arr[0]

                if (word != "-1"):
                    if (result == ""):
                        # result = result + "{" + word
                        result.append(word)
                    else:
                        # result = result + " , " + word
                        result.append(word)
                index += 1


file = open('output.txt', 'w')
formatted_result = []
for r in result:
    # file.write(FunctionsClass.print(r))
    # format = r.replace("'\\", "\\\'")

    format = FunctionsClass.print(r)
    formatted_result.append(format)
#     output = "".join(formatted_result)
# output = '"' + output + '"'
    file.write(format)

file.close()
