cube = lambda x: x * x * x

def fibonacci(n):
   if n == 1:
       return [0]
   if n == 2:
       return [0, 1]
   arr = [0, 1]
   for i in range(n - 2):
       arr.append(arr[-1] + arr[-2])
   return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
