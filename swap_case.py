s = input()
res = ""
for i in s:
    if 65 <= ord(i) <= 90:
        res += chr(ord(i) + 97 - 65)
    elif 97 <= ord(i) <= 122:
        res += chr(ord(i) - (97 - 65))
    else:
        res += i
print(res)
