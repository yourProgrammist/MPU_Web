n = int(input())
if (n % 2 == 0 and 6 <= n <= 20) or (n % 2 == 1):
    print("Weird")
if (n % 2 == 0) and (n > 20 or 2 <= n <= 5):
    print("Not Weird")
