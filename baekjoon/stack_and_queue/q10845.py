# 큐
import sys

queue = []


def operate_queue(command):
    global queue
    if command.startswith("push"):
        p, n = command.split()
        queue.append(int(n))

    elif command == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            del queue[0]

    elif command == 'size':
        print(len(queue))

    elif command == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif command == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    else: ## back
        if not queue:
            print(-1)
        else:
            print(queue[-1])


n = int(sys.stdin.readline().strip())
for _ in range(n):
    command = sys.stdin.readline().strip()
    operate_queue(command)

