def mul(a, b):
    sum = 0
    for i in range (b):
        sum += a
    return sum

def mul2(a,b):
    sum = 0
    i = 0
    while (i < b):
        sum += a
        i += 1
    return sum

def expo(a, b):
    pro = 1
    j = 0
    i = 0
    sum = 0
    while (j < b):
        j += 1
        i = 0
        sum = 0
        while (i < a):
            i += 1
            sum += pro
        pro = sum
    return pro




def main():
    print(mul(2, 7))
    print(mul2(2, 7))
    print(expo(3, 4))
    return 0


if __name__ == '__main__':
    main()