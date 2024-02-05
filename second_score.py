n = int(input())
arr = list(set(map(int, input().split())))
if (len(arr) < 2):
    print("Not second place")
else:
    arr.sort(reverse=True)
    print(arr[1])
