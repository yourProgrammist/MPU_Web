from collections import Counter
res = []
mx_size = -1
with open("example.txt", 'r') as f:
    for line in f:
        for word in line.split():
            new_word = ""
            for letter in word:
                if letter.isalnum():
                    new_word += letter
            if (mx_size < len(new_word)):
                res = [new_word]
                mx_size = len(new_word)
            elif (mx_size == len(new_word)):
                res.append(new_word)
for val in Counter(res):
    print(val)

                    

