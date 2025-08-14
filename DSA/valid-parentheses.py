def valid_parethese(str):
    mapping = {")":"(","}":"{","]":"["}
    stack = []
    print("mapping.values()",mapping.values())
    for char in str:
        print("-----1",char)
        if char in mapping.values():
            stack.append(char)
            print("--------2", stack)
        elif char in mapping:
            print("-------3", char)
            print("--------4",mapping[char])
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack

a = valid_parethese("()")
print(a)