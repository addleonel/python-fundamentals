def balanced(expression):
    stack_list = []
    for letter in expression:
        if letter == '(':
            stack_list.insert(0, letter)
        elif letter == ')':
            if '(' in stack_list:
                stack_list.pop(0)
            else:
                stack_list.insert(0, 'nop')
    if stack_list:
        return False
    return True


if __name__ == '__main__':
    print(balanced(input()))
