msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msgs = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5,
        msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

memory = 0
result = 0


def is_one_digit(a):
    return a.is_integer() and 10 > a > -10


def check(a, b, c):
    msg = ''
    if is_one_digit(a) and is_one_digit(b):
        msg += msg_6
    if (a == 1 or b == 1) and c == '*':
        msg += msg_7
    if (a == 0 or b == 0) and (c == '*' or c == '+' or c == '-'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


while True:
    while True:
        calc = input(msg_0)
        x, oper, y = calc.split()

        if x == 'M':
            x = memory
        if y == 'M':
            y = memory

        try:
            x = float(x)
            y = float(y)

        except ValueError:
            print(msg_1)
            continue
        else:
            if oper not in ['-', '+', '/', '*']:
                print(msg_2)
                continue
            check(x, y, oper)
            if oper == '+':
                result = x + y
            elif oper == '-':
                result = x - y
            elif oper == '*':
                result = x * y
            elif oper == '/':
                if y != 0:
                    result = x / y
                else:
                    print(msg_3)
                    continue
            print(result)
            break
    cont = True
    while True:
        if not cont:
            break
        print(msg_4)
        answer = input()
        if answer != 'y':
            if answer != 'n':
                continue
            break
        else:
            if not is_one_digit(result):
                memory = result
                break
            else:
                msg_index = 10
                while True:
                    print(msgs[msg_index])
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            cont = False
                            break
                    else:
                        if answer == 'n':
                            cont = False
                            break
                        else:
                            continue

    should_continue = ''
    while True:
        print(msg_5)
        should_continue = input()
        if should_continue == 'y':
            break
        else:
            if should_continue != 'n':
                continue
            else:
                break
    if should_continue == 'y':
        continue
    else:
        break
