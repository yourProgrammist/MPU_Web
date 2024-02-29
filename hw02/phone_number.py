def wrapper(f):
    def fun(l):
        res = []
        for number in l:
            ans = '+7 ('
            for index, i in enumerate(number):
                if index == 0 and i in ['0', '7', '8']:
                    continue
                if len(ans) == 7:
                    ans += ') '
                if len(ans) == 12:
                    ans += '-'
                if len(ans) == 15:
                    ans += '-'
                ans += i
            res.append(ans)
        return sorted(res)
    return fun

@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')
# 07895462130