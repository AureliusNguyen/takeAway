import random

def main():
    sum = 21
    while (sum > 0):
        if (sum > 3):
            b = random.randint(1,3)
            print(f"{sum} objects remain, I'll take {b}")
            z = int(input(f"{sum - b} objects remain, choose 1, 2, or 3: "))
            sum -= b
            while (z != 1 and z != 2 and z != 3):
                print("Invalid option, try again.")
                z = int(input(f"{sum} objects remain, choose 1, 2, or 3: "))
            sum -= z
            if (sum == 0):
                print("You win!")
        else:
            print("I win!")
            break


    return 0


if __name__ == '__main__':
    main()