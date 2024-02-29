import time
def process_list(arr):
    result = []
    for i in arr:
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)
    return result

def process_list_gen(arr):
    return [i ** 2 if i % 2 == 0 else i ** 3 for i in arr]


if __name__ == '__main__':
    start = time.time()
    print(process_list_gen([1, 2, 3, 7, 9, 1, 2, 8]))
    end = time.time() - start
    print(end)
    print(process_list([1, 2, 3, 7, 9, 1, 2, 8]))


# 0.0000467300415039 process_list_gen
# 0.0000050067901611 process_list