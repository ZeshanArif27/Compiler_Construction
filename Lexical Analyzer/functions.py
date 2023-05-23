import re


class Token:
    def __init__(self):
        CP = "None"
        Vp = ""
        Line_no = 0
    CP = None
    VP = ""
    Line_no = None


keyWord = {
    "import": "import", "from": "from", "in": "in", "func": "func", "if": "if", "else": "else", "obj": "obj",
    "while": "while", "for": "for", "continue": "continue", "break": "break", "return": "return", "array": "array",
    "bool": "DT", "int": "DT",  "float": "DT", "char": "DT", "str": "DT", "class": "class", "final": "final",
    "inherits": "inherits", "static": "static", "this": "this", "super": "super", "abstract": "abstract",
    "construct": "construct", "public": "public", "private": "private"
}

operaTors = {
    ":=": ":=", "!=": "Relational Operator", "==": "Relational Operator", "<": "Relational Operator", "->": ".", ">": "Relational Operator", ">=": "Relational Operator", "<=": "Relational Operator", "*": "*", "||": "||", "&": "&", "+": "Plus", "-": "Minus", "*": "Multiply", "/": "Divide", "%": "Modulus", "++": "Increment", "--": "Decrement", "+=": "Compound Assignment", "-=": "Compound Assignment", "*=": "Compound Assignment", "/=": "Compound Assignment", "=": "Assignment Operator"
}

puncTuators = {
    ".": ".", ";": ";", "{": "{", "}": "}", ",": ",", "[": "[", "]": "]", "(": "(", ")": ")", ":": ":", "'": "'", '"': '"', "'\n": "New Line", "\\'": "Backslash"
}


class FunctionsClass:
    def __init__(self):
        pass

    def isKeyword(user_input):
        for i in keyWord.keys():
            if (i == user_input):
                return keyWord[i]

        return None

    def isOperator(user_input):
        for i in operaTors.keys():
            if (i == user_input):
                return operaTors[i]

        return None

    def isPunctuator(user_input):
        for i in puncTuators.keys():
            if (i == user_input):
                return puncTuators[i]

        return None

    def isCharConst(user_input):
        is_matched = bool(re.fullmatch("^'[A-Za-z]'$", user_input))
        return is_matched

    def isNumber(user_input):
        is_matched = bool(re.match('[+-]?\d+[.\d]*', user_input))
        return is_matched

    def int_check(user_input):

        is_matched = bool(re.match('^[+-]?[0-9]+$', user_input))
        return is_matched

    def isAlpha(user_input):
        is_matched = bool(re.match('^[A-Za-z]+$', user_input))
        return is_matched

    def isIntConst(user_input):
        is_matched = bool(re.match('^[+-]?[0-9]+$', user_input))
        return is_matched

    def isFloatConst(user_input):
        is_matched = bool(re.match('^[+-]?[0-9]*[.][0-9]+$', user_input))
        return is_matched

    def isStringConst(user_input):
        if (FunctionsClass.isCharConst(user_input) == False):
            is_matched = bool(re.fullmatch('"{1}.*"{1}', user_input))
            return is_matched

    def isBoolConst(user_input):
        if (user_input == "True" or user_input == "False"):
            return True

    def isIdentifier(user_input):
        is_matched = bool(re.fullmatch(
            '^[a-zA-Z][a-zA-Z0-9]*(_[A-Za-z0-9]+)*|[_][A-Za-z0-9]+(_[A-Za-z0-9]+)*$', user_input))
        return is_matched

    def print(result):
        # result = "".join("[" + result + "],")
        return "" + result + ","
