def div27(num):
    out = False
    for i in range(2,8):
        if num % i == 0:
            out = True
            break
        else:
            out = False
    return out


def main():
    print(div27(15)) #Should return True
    return 0

if __name__ == '__main__':
    main()