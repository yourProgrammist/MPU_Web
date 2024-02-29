import sys
def my_sum(args):
    return sum(int(x) for x in args)


if __name__ == "__main__":
    print(my_sum(sys.argv[1:]))