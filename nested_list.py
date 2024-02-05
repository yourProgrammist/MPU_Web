n = int(input())
arr = []
for i in range(n):
    name = input()
    grade = float(input())
    arr.append([name, grade])
arr.sort(key=lambda x: (x[1], x[0]))
m = list(set([x[1] for x in arr]))
if (len(m) < 2):
    print("Not second grade")
else:
    for i in arr:
        if i[1] == sorted(m)[1]:
            print(i[0])
    

