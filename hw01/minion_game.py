s = input()
vowels = "AEIOU"
cnt_f = 0
cnt_s = 0
len_s = len(s)

for i in range(len_s):
    if s[i] in vowels:
        substring = ""
        for j in range(i, len_s):
            substring += s[j]
            cnt_f += 1
    else:
        substring = ""
        for j in range(i, len_s):
            substring += s[j]
            cnt_s += 1
if cnt_f > cnt_s:
    print(f'Кевин {cnt_f}')
else:
    print(f'Стюарт {cnt_s}')