n = int(input("Check this number: "))


def prime_checker(number):
    if number > 1:
        for x in range(2, number):
            if number % x == 0:
                print("It's not a prime number.")
                return
        print("It's a prime number")
    else:
        print("The number is below one.")


prime_checker(number=n)
