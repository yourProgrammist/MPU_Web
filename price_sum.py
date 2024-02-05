arr = [0, 0, 0]
with open("products.csv", 'r') as f:
    header = 1
    for line in f:
        if header:
            header = 0
        else:
            prices = line.split(',')[1:]
            for i in range(len(prices)):
                arr[i] += float(prices[i].strip())
print(*[round(x, 2) for x in arr])

                
