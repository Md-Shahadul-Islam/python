def push(X, stack):
    stack.append(X)

def pop(stack):
    if not stack:
        return '!'
    else:
        return stack.pop()



def top(stack):
    return stack[-1]

def infix_to_postfix(infix):
    postfix = []
    stack = []
    i = 0

    while i < len(infix):
        s = infix[i]
        if s in ['+', '-', '*', '/']:
            while stack and priority(top(stack)) >= priority(s):
                postfix.append(pop(stack))
            push(s, stack)
        elif s == '(':
            push(s, stack)
        elif s == ')':
            while stack and top(stack) != '(':
                postfix.append(pop(stack))
            pop(stack)  
        else:
            postfix.append(s)
        i += 1

    while stack:
        postfix.append(pop(stack))

    return postfix

infix = input("Enter Infix: ")
postfix = infix_to_postfix(infix)
print("Postfix:", ' '.join(postfix))
