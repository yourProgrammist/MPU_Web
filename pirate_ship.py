n, m = map(int, input().split())
arr = []
for i in range(m):
    name, p, price = input().split()
    arr.append([name, float(p), float(price), float(price) / float(p)])
arr.sort(key=lambda x: -x[3])
for name, p, price, x in arr:
    if p < n:
        n -= p
        print(name, p, price)
    else:
        print(name, n, round(price * n / p, 2))
        break
