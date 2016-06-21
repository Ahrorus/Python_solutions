#Card game

head1 = 0
head2 = 0
i = 0

def push1(x):
    first.append(x)

def pop1():
    global head1
    head1 += 1
    return first[head1 - 1]

def push2(x):
    second.append(x)

def pop2():
    global head2
    head2 += 1
    return second[head2 - 1]

first = [int(s) for s in input().split()]
second = [int(s) for s in input().split()]

while abs(len(first) - len(second)) < 10:
    i += 1
    if i == 1000000:
        break
    a = pop1()
    b = pop2()
    if a > b and a != 0 and b != 0:
        push1(b)
        push1(a)
    elif b > a and a != 0 and b != 0:
        push2(a)
        push2(b)
    elif a == 0:
        push1(b)
        push1(a)
    else:
        push2(a)
        push2(b)

if i == 1000000:
    print("botva")
elif len(first) > len(second):
    print("first ", i)
else:
    print("second ", i)

