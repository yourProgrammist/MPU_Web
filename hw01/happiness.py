n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
cnt = 0
for i in arr:
    if i in A:
        cnt += 1
    elif i in B:
        cnt -= 1
print(cnt)
