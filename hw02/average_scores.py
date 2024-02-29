def compute_average_scores(scores):
    return [sum(scores[j][index] for j in range(len(scores))) / len(scores) for index in range(len(scores[0]))]


if __name__ == "__main__":
    n, x = map(int, input().strip().split())
    arr = []
    for i in range(x):
        arr.append(tuple(map(float, input().split())))
    for _ in compute_average_scores(arr):
        print(_)