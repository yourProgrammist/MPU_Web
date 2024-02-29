arr = []
cnt = 0
for i in range(int(input())):
    i_n, ou_t = map(int, input().split())
    arr.append([i_n, ou_t])
t = int(input()) # считаю, что задано оно тоже от начала работы метрополитена
for x, y in arr:
    if x <= t < y:
        cnt += 1
print(cnt)

