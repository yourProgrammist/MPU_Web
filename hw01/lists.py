arr = []
for i in range(int(input())):
    command, *val = input().split()
    if command == "append" and len(val) > 0:
        arr.append(int(val[0]))
    elif command == "print":
        print(arr)
    elif command == "insert" and len(val) > 1:
        arr.insert(int(val[0]), int(val[1]))
    elif command == "remove" and len(val) > 0:
        if int(val[0]) in arr:
            arr.remove(int(val[0]))
    elif command == "sort":
        arr.sort()
    elif command == "pop":
        arr.pop()
    elif command == "reverse":
        arr.reverse()



