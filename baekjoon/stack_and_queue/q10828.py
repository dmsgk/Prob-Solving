# 스택

import sys
stack = []

def push(n):
    global stack
    stack.append(n)


def stack_pop():
    global stack
    if not stack:
        print(-1)
    else:
        print(stack[-1])
        del stack[-1]


def size():
    global stack
    print(len(stack))

def empty():
    global stack
    if stack:
        print(0)
    else:
        print(1)

def top():
    global stack
    if stack:
        print(stack[-1])
    else:
        print(-1)


n = int(sys.stdin.readline())
for _ in range(n):
    commands = sys.stdin.readline().strip()

    # print(stack, commands)


    if commands.startswith("push"):
        p, n = commands.split()
        push(int(n))
    elif commands == 'pop':
        stack_pop()
    elif commands == 'size':
        size()
    elif commands == 'empty':
        empty()
    else:
        top()
