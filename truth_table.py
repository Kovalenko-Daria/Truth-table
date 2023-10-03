from itertools import product

def prior(sym):
    if sym == '~':
        return 1
    elif sym == '^':
        return 2
    elif sym == '->':
        return 3
    elif sym == 'or':
        return 4
    elif sym == 'and':
        return 5
    elif sym == 'not':
        return 6

def oper(a, b, op):
    if op == '~':
        return a == b
    elif op == '^':
        return a != b
    elif op == '->':
        return a <= b
    elif op == 'or':
        return a or b
    elif op == 'and':
        return a and b

def get_lexems_var():
    lexems = input().replace('(', '( ').replace(')', ' )')
    lexems = lexems.split()
    var = sorted(list(set([i for i in lexems if 'A' <= i <= 'Z'])))
    return lexems, var

def polish_notation(lexems, var):
    queue = []
    stack = []
    for i in lexems:
        if i == ')':
            for j in range(len(stack) - 1, -1, -1):
                if stack[j] == '(':
                    stack.pop()
                    break
                queue.append(stack.pop())
        elif i == '(':
            stack.append(i)
        elif i in var:
            queue.append(i)
        elif i == "0" or i == "1":
            queue.append(int(i))
        else:
            while len(stack) > 0 and stack[-1] != '(' and prior(i) <= prior(stack[-1]):
                queue.append(stack.pop())
            stack.append(i)
    for i in range(len(stack) - 1, -1, -1):
        queue.append(stack.pop())
    return queue

def count_value(var, value, queue):
    var_value = {variable: element for variable, element in [
            (var[j], value[j]) for j in range(len(var))]}
    comput_list = []
    for j in queue:
        if j in var:
            comput_list.append(var_value[j])
        elif j == 0 or j == 1:
            comput_list.append(j)
        elif j == 'not':
            comput_list[-1] = not comput_list[-1]
        else:
            comput_list[-2] = oper(comput_list[-2], comput_list[-1], j)
            comput_list.pop()
    return int(comput_list[0])

def perform_truth_table():
    lexems, var = get_lexems_var()
    queue = polish_notation(lexems, var)
    print(*var, sep=' ', end=' ')
    print('F')
    comb_value = list(product(*([[0, 1]] * len(var))))
    for i in comb_value:
        print(*i, sep=' ', end=' ')
        print(count_value(var, i, queue))

perform_truth_table()