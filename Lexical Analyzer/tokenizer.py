import functions


def tokenizer(filename):
    file = open(filename, 'r')
    content = file.read()
    words = content.split(',')
    tokenList = []
    count = 1
    for word in words:
        token = functions.Token()
        if ('\n' in word):
            count += 1
        if ('/*' in word):
            pass
        if (word != -1):
            if (word == '_'):
                if (functions.FunctionsClass.isIdentifier(word)):
                    token.CP = "ID"
                    token.VP = word
                    token.Line_no = count
                    tokenList.append(token)
                else:
                    token.CP = "Invalid token"
                    token.VP = word
                    token.Line_no = count
                    tokenList.append(token)
            elif (functions.FunctionsClass.isNumber(word)):
                temp = functions.FunctionsClass.isIntConst(word)
                if (temp):
                    token.CP = "Int Const"
                    token.VP = word
                    token.Line_no = count
                    tokenList.append(token)
                else:
                    temp = functions.FunctionsClass.isFloatConst(word)
                    if (temp):
                        token.CP = "Float Const"
                        token.VP = word
                        token.Line_no = count
                        tokenList.append(token)
                    else:
                        token.CP = "Invalid token"
                        token.VP = word
                        token.Line_no = count
                        tokenList.append(token)
            elif (word == '.'):
                if len(word) > 1:
                    temp = functions.FunctionsClass.isFloatConst(word)
                    if (temp):
                        token.CP = "Float Const"
                        token.VP = word
                        token.Line_no = count
                        tokenList.append(token)
                    else:
                        token.CP = "Invalid token"
                        token.VP = word
                        token.Line_no = count
                        tokenList.append(token)
                else:
                    token.CP = "."
                    token.VP = word
                    token.Line_no = count
                    tokenList.append(token)
            elif (functions.FunctionsClass.isBoolConst(word) and functions.FunctionsClass.isKeyword(word) == None):
                token.CP = "Bool Const"
                token.VP = word
                token.Line_no = count
                tokenList.append(token)

            elif (functions.FunctionsClass.isAlpha(word)):
                temp = functions.FunctionsClass.isIdentifier(word)
                if (temp):
                    classPart = functions.FunctionsClass.isKeyword(word)
                    if (classPart != None):
                        token.CP = classPart
                        token.VP = word
                        token.Line_no = count
                        tokenList.append(token)
                    else:
                        token.CP = "ID"
                        token.VP = word
                        token.Line_no = count
                        tokenList.append(token)
                else:
                    token.CP = "Invalid token"
                    token.VP = word
                    token.Line_no = count
                    tokenList.append(token)
            else:
                punc = functions.FunctionsClass.isPunctuator(word)
                oprt = functions.FunctionsClass.isOperator(word)
                if (punc != None):
                    token.CP = punc
                    token.VP = word
                    token.Line_no = count
                    tokenList.append(token)
                elif (oprt != None):
                    token.CP = oprt
                    token.VP = word
                    token.Line_no = count
                    tokenList.append(token)
                else:
                    token.CP = "Invalid token"
                    token.VP = word
                    token.Line_no = count
                    tokenList.append(token)

            count += 1

    tok = functions.Token()
    tok.CP = "$"
    tok.VP = "$"
    tok.Line_no = count
    tokenList.append(tok)
    return tokenList


# filename = 'output.txt'
# with open(filename, 'r') as files:
#     content = files.read()
#     array = content.split(',')
#     out = open('out.txt', 'w')
# for output in array:
#     out.write(output)


token = tokenizer('output.txt')
file = open('token_output.txt', 'w')
for item in token:
    file.write('"'+item.CP + '", "' + item.VP +
               '", "' + str(item.Line_no) + '" ''\n')

file.close()
